from django.urls import path
from . import views

app_name = 'utl_app'

urlpatterns = [
    path('', views.home, name='home'),                    # For inputting a URL
    path('<str:shortcode>/', views.redirect_url, name='redirect'),  # For redirection
]
