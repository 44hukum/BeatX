from django.urls import path
from . import views
app_name='songs'
urlpatterns=[
    path('',views.index,name='index'),
    path('searchMusic/',views.searchMusic,name='searchMusic'),
    path('profile/',views.profile,name='profile'), #shows the profile of the user
]
