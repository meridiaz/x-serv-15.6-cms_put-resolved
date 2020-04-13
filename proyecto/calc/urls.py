from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('sumar/<int:op1>/<int:op2>', views.add),
    path('restar/<int:op1>/<int:op2>', views.sub),
    path('multiplicar/<int:op1>/<int:op>', views.multi),
    path('dividir/<int:op1>/<int:op2>', views.div),
]
