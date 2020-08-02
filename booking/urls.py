from django.urls import path, include
from booking import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
    path('booking/<int:pk>/', views.booking, name='booking'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard_update/<int:pk>/', views.update_dashboard, name='dashboard_update'),
    path('customer', views.customer_signup, name='customer_signup'),
    path('staff', views.staff_signup, name='staff_signup'),
]