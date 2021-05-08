from django.shortcuts import render
from .models import *
def home(request):
  views={}
  views['reviews']=Review.objects.all()
  return render(request,'index.html',views)

def about(request):
  return render(request, 'about.html')

def service(request):
  return render(request,'services.html')

def price(request):
  return render(request, 'price.html')

def portfolio(request):
  return render(request, 'portfolio.html')

def elements(request):
  return render(request, 'elements.html')

def contacts(request):
  views={}
  views['information']=Information.objects.all()
  if request.method == "POST":
    my_name = request.POST['name']
    my_email = request.POST['email']
    my_subject = request.POST['subject']
    my_message = request.POST["message"]
    data = Form.objects.create(
      name=my_name,
      email=my_email,
      subject=my_subject,
      message=my_message

     )
    data.save()
    views['msg']='your query has been enrolled. Thank you'
    return render(request,'contact.html', views)
  return render(request, 'contact.html',views)

def blog_single(request):
  return render(request, 'blog-single.html')

def blog_home(request):
  return render(request, 'blog-home.html')