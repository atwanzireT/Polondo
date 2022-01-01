import json
from django.shortcuts import render
from user.models import *
from order.views import shopcart
from .models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from Polondo import settings
from products.models import *
from .forms import SearchForm
from order.models import *

# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_latest = Product.objects.all().order_by('-id')[:4]  # last 4 products
    products_slider = Advert.objects.all().order_by('?')[:4]  #first 4 products
    products_picked = Product.objects.all().order_by('?')[:4]   #Random selected 4 products
    page="home"
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    total=0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    context={
            'total':total,
            'setting':setting,
            'page':page,
            'shopcart':shopcart,
            'products_slider': products_slider,
            'products_latest': products_latest,
            'products_picked': products_picked,
            'category':category
             }
    return render(request,'index.html',context)
def about(request):
    setting = Setting.objects.get(pk = 1)
    category = Category.objects.all()

    context = {
        'setting': setting,
        'category': category,
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact/')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm
    context={'setting':setting,'form':form, 'category':category  }
    return render(request, 'contact.html', context)

def category_products(request,id,slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id) 
    setting = Setting.objects.get(pk=1)
    context={
        'products': products,
        'setting': setting,
        'category': category,
            }
    return render(request, 'category_products.html', context)

def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title +" > " + rs.category.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    picked = Product.objects.filter(category = product.category).order_by("?")
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id,status='True')
    comments_length = Comment.objects.filter(product_id=id,status='True').count()
    context = {
        'product':product,
        'category':category,
        'images':images,
        'comments':comments,
        'comments_length':comments_length,
        'picked':picked
    }
    return render(request,'product_detail.html',context)