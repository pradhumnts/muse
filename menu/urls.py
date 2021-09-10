from django.urls import path

from . import views

urlpatterns = [
    # ex: /menu/
    path('', views.index, name='index'),
    path('additem', views.add_item, name='additem'),
]