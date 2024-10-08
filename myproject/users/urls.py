from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    
    
    
    path('posts/', views.post_list, name='post-list'),
    path('posts/create/', views.create_post, name='create-post'),
    path('posts/update/<int:pk>/', views.update_post, name='update-post'),
    path('posts/delete/<int:pk>/', views.delete_post, name='delete-post'),
]
