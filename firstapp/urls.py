from django.urls import path
from firstapp import views

app_name="basicapp"
urlpatterns = [

path('',views.index,name="index"),
path('add/',views.add,name="add")

]
