from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='client_app'

urlpatterns =[
    path('', views.Index.as_view(), name='indexpage'),
    path('details/<int:pk>/', views.SingleProduct.as_view(), name='singlepage'),
    path('profile/<int:pk>/', views.profileView, name='profileInfo'),
    path("register/", views.registerView, name="register"),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView,name='thanks'),
]