from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:topics>/', views.topics, name='topics'),
]