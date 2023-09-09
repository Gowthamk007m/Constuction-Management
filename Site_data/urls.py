from django.urls import path
from . views import *

urlpatterns = [
    path('',home_page,name='home'),
    path('all_user/', all_user, name='all_user'),
    path('add_site/', add_site, name='add_site'),
    path('site_user_create/', site_user_create, name='site_user_create'),
    path('add_new_site/', add_new_site, name='add_new_site'),
    path('add_new_user/', create_user, name='create_user'),



]