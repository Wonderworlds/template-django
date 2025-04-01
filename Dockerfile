# Use the official PostgreSQL image from the Docker Hub
FROM postgres:latest

# Set environment variables for PostgreSQL
# You can customize these variables as needed
ENV POSTGRES_USER=djangouser
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_DB=djangotraining

# Expose the default PostgreSQL port
EXPOSE 5432

# Command to run PostgreSQL
CMD ["postgres"]
