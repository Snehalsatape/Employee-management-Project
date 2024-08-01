from django.urls import path
from . import views

app_name = 'empapp'

urlpatterns = [
    path('search/', views.search_form, name='search'),
]
