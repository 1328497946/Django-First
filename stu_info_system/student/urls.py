from django.urls import path
from .views import *

urlpatterns = [
	path('', home),
	path("slogin/", slogin),
	path("modify/", modify),
	path('slogout/', slogout),
]
