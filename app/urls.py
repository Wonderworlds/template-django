from .views import Home, Login, SignUp, Logout
from django.urls import path


urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
]
