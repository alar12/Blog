
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import UserProfile
from .forms import BlogForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
# blog/views.py


def home(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'home.html',{'blog_posts': blog_posts})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # Save the blog post
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Assuming you have an 'author' field in your model
            blog_post.save()
            return redirect('home')  # Redirect to the home page or wherever you want
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

# blogs/views.py


def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})
