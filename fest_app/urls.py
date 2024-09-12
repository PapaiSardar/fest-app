from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name='home'),
    path("home",views.home),
    path("photos",views.photos),
    path("event",views.events),
    

    
    
]