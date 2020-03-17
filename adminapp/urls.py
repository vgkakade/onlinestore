from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name='admin_app'

urlpatterns =[
    path('', views.BooksListView.as_view(), name='adminhome'),
    path('addproduct/', views.AddBookView.as_view(), name='add_book'),
    url(r'^(?P<pk>\d+)/', views.UpdateView.as_view(), name='book_update'),
    url(r'^delete/(?P<pk>\d+)/', views.BookDeleteView.as_view(), name='book_delete'),
    path('login/', auth_views.LoginView.as_view(template_name="admin_login.html"), name='login'),
]