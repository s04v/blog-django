from django.shortcuts import render, redirect
from django.views.generic.base import View 
from .models import Post
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.shortcuts import render, HttpResponseRedirect

class PostView(View):
  def get(self, request):
    admin_token  = request.COOKIES.get("token")
    is_logged = False
    if admin_token == "x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi":
      is_logged = True

    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': posts, 'is_logged': is_logged}) 

class SpecificPost(View):
  def get(self, request, id):
    admin_token  = request.COOKIES.get("token")
    is_logged = False
    if admin_token == "x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi":
      is_logged = True

    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post, 'is_logged': is_logged}) 
  
class NewPost(View): 
  def get(self, request):
    admin_token  = request.COOKIES.get("token")
    if admin_token != "x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi":
      return redirect('/blog')
      
    is_logged = False
    if admin_token == "x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi":
      is_logged = True

    return render(request, 'blog/new-post.html', {'is_logged': is_logged}) 

  def post(self, request):
    form = PostForm(request.POST)
    if form.is_valid():
      form = form.save()

    return redirect('/')   

# admin token = x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi
class Login(View):
  def get(self, request):
    return render(request, 'blog/login.html')

  def post(self, request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'admin' and password == 'admin':
      response = HttpResponseRedirect("/")
      response.set_cookie(key="token", value="x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi")
      return response
    return redirect('/login')

class EditPost(View):
  def get(self, request, id):
    admin_token  = request.COOKIES.get("token")
    if admin_token != "x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi":
      return redirect('/')

    is_logged = False
    if admin_token == "x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi":
      is_logged = True
    
    post = Post.objects.get(id=id)
    return render(request, 'blog/edit.html', {'post': post, 'is_logged': is_logged}) 
  
  def post(self, request, id):
    admin_token  = request.COOKIES.get("token")
    if admin_token != "x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi":
      return redirect('/')

    post = Post.objects.get(id=id)
    post.title = request.POST['title']
    post.text = request.POST['text']
    post.save()
    return redirect('/')   


class DeletePost(View):
  def get(self, request, id):
    admin_token  = request.COOKIES.get("token")
    if admin_token != "x5m2NVOky5Y9U753hdlQ5fae8UjEDtWi":
      return redirect('/')

    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')


class Logout(View):
  def get(self, request):
    response = HttpResponseRedirect("/")
    response.delete_cookie("token")
    return response