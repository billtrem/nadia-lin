from django.shortcuts import render, get_object_or_404
from .models import HomepageImage, InfoPageContent, BlogPost, Exhibition, Product

def home(request):
    images = HomepageImage.objects.all()
    return render(request, 'main/home.html', {'images': images})

def info(request):
    info = InfoPageContent.objects.first()
    return render(request, 'main/info.html', {'info': info})

def blog_list_view(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'main/blog_list.html', {'posts': posts})

def blog_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'main/blog_detail.html', {'post': post})

def exhibitions(request):
    exhibitions = Exhibition.objects.all().order_by('-date')
    return render(request, 'main/exhibitions.html', {'exhibitions': exhibitions})

def shop(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'main/shop.html', {'products': products})
