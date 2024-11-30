from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('classify/', views.classify_breast_cancer, name='classify_breast_cancer'),
]
