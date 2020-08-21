from django.urls import path
from . import views

app_name = 'godkids'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:security_code>/', views.detail, name='detail')
]
