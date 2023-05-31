from django.urls import path
from . import views

urlpatterns = [
  path('', views.PostView.as_view()),
  path('post/<int:id>/', views.SpecificPost.as_view()),
  path('edit/<int:id>/', views.EditPost.as_view()),
  path('delete/<int:id>/', views.DeletePost.as_view()),
  path('new-post', views.NewPost.as_view()),
  path('login', views.Login.as_view()),
  path('logout', views.Logout.as_view())
]