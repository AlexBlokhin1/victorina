from django.urls import path, include
from victorina import views

urlpatterns = [
    path(r'', views.homepage, name='homePageVictorina'),
    path(r'victorinaPage/', views.get_victorina, name='victorinaPage'),
]
