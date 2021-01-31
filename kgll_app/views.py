from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Slider
from .models import Team
from .models import Posts
from .models import Product
from django.http import HttpResponse

# Create your views here.


def index(request):
    slider = Slider.objects.all()
    context = {'slider': slider}
    return render(request, 'index.html', context)


def products(request):
    product = Product.objects.all()
    product_context = {'product': product}
    return render(request, 'products.html', product_context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("txtName")
        email = request.POST.get("txtEmail")
        phone_number = request.POST.get("txtPhone")
        message = request.POST.get("txtMsg")
        print(name, email, phone_number, message)
        return redirect
        
    return render(request, 'contact.html', {})


def about(request):
    team = Team.objects.all()
    team_context = {'team': team}
    return render(request, 'about.html', team_context)


def updates(request):
    posts = Posts.objects.all()
    post_context = {'posts': posts}
    return render(request, 'updates.html', post_context)


class PostListView(ListView):
    model = Posts
    template_name = 'updates.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Posts
    template_name = 'post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def post(request):
    return render(request, 'post.html', {})
