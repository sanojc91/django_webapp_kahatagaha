from django.urls import path
from .views import PostListView, PostDetailView
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products', views.products, name="products"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('updates', views.updates, name="updates"),
    path('post', PostListView.as_view(), name="post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
]
