from django.shortcuts import render,render_to_response

def home(request):
	return render(request,'index.html')

def blog(request):
	return render(request,'blog.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')