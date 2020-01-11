from django.urls import path
from .views import helloworld,index,UserView,message_post
app_name = "home"
urlpatterns = [
    path('helloworld/',helloworld,name="helloworld"),
    path('homepage/',index,name="homepage"),
    path('homepage/<int:user_id>',UserView.as_view(),name="page"),
    path('homepage/form/',message_post,name="form"),
]