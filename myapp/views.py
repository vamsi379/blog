from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Blog

# Create your views here.
def index(request):
	#processing here
	blogs = Blog.objects.all()
	context = {'blogs':blogs}
	return render(request,'index.html',context)

def detail(request,pk):
	blog = Blog.objects.get(pk = pk)
	context = {'blog':blog}
	return render(request,'detail.html',context)
