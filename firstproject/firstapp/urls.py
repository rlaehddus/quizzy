from django.urls import path
from . import views

app_name = 'firstapp'
urlpatterns = [
    path('', views.main),
    path('one/', views.one, name="page_one"),
    path('two/', views.two, name="page_two"),
    path('three/', views.three, name="page_three"),
]