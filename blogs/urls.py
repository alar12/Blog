# blog/urls.py

from django.urls import path,include
from blogs.views import home, register, user_login,create_blog ,user_logout ,blog_detail# Check this import path

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('create_blog/', create_blog, name='create_blog'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),  # Add this line
    path('logout/', user_logout, name='logout'),
]
