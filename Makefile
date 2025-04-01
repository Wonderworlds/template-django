python := python3
SRC_DIR := .
VENV_DIR := django_venv
DEP_FILE := requirements.txt
PROJECT_DIR := d09

DOCKER_IMG_NAME := postgres-img
DOCKER_CONTAINER_NAME := postgres-container

define venvWrapper
	{\
	. $(VENV_DIR)/bin/activate; \
	$1; \
	}
endef

APP_FILE := manage.py

help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  start:    	 Run the project"
	@echo "  install:    Install the project"
	@echo "  freeze:     Freeze the dependencies"
	@echo "  fclean:     Remove the virtual environment and the datasets"
	@echo "  clean:      Remove the cache files"
	@echo "  re:         Reinstall the project"
	@echo "  phony:      Run the phony targets"

start:
	@$(call venvWrapper, $(python) $(APP_FILE) runserver)

init-project:
	@$(call venvWrapper, django-admin startproject ${PROJECT_DIR} .)

create-app:
	@$(call venvWrapper, ${python} $(APP_FILE) startapp ${ARG})

run-docker:
	docker build -t $(DOCKER_IMG_NAME) .
	docker run -d --name $(DOCKER_CONTAINER_NAME) -p 5432:5432 $(DOCKER_IMG_NAME)

prune-docker:
	docker stop $(DOCKER_CONTAINER_NAME)
	docker rm $(DOCKER_CONTAINER_NAME)
	docker rmi $(DOCKER_IMG_NAME)

migrate:
	@$(call venvWrapper, ${python} $(APP_FILE) migrate)

install:
		@{ \
		echo "Setting up..."; \
		if [ -z ${ASSET_URL} ] || [ -d ${DATA_DIR}  ]; then echo "nothing to download"; else \
			wget --no-check-certificate -O dataset.zip ${ASSET_URL}; \
			mkdir -p ${DATA_DIR}/; \
			tar -xvf dataset.zip -C ${DATA_DIR}/; \
			rm -rf dataset.zip; \
		fi; \
		python3 -m venv ${VENV_DIR}; \
		. ${VENV_DIR}/bin/activate; \
		if [ -f ${DEP_FILE}  ]; then \
			pip install --force-reinstall -r ${DEP_FILE}; \
			echo "Installing dependencies...DONE"; \
		fi; \
		}

freeze:
	$(call venvWrapper, pip freeze > ${DEP_FILE})

fclean: clean
	rm -rf bin/ include/ lib/ lib64 pyvenv.cfg share/ etc/ $(VENV_DIR) db.sqlite3

clean:
	rm -rf ${SRC_DIR}/__pycache__ */**/**/__pycache__ */**/__pycache__ */__pycache__

re: fclean install

phony: install freeze fclean clean re help