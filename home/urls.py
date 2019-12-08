from django.urls import path
from .views import helloworld,index
app_name = "home"
urlpatterns = [
    path('helloworld/',helloworld,name="helloworld"),
    path('homepage/',index,name="homepage"),
]