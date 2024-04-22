from django.shortcuts import render
from books.models import *
from django.http import HttpResponse
# Create your views here.

def Index(request):
    return render(request,'index.html')
def BookGet(request):
    if request.method=='POST':
        
          title=request.POST['title']
          author=request.POST['author']
          description=request.POST['description']
          book=Book.objects.create(title=title,author=author,description=description)    
    return render(request,'book.html')
def Details(request):
    books=Book.objects.all().values()
    context = {
        'books':books
    }
    return render(request,'book.html',context)

def Search(request):
     if request.method=='POST':
        title=request.POST['title']
        books=Book.objects.filter(title__icontains=title).values()
        book=Book.objects.filter(title__icontains=title).count()
        if book>0:
            context = {
             'books':books
                }
            return render(request,'search.html',context)
        else:
             
             return render(request,'searchError.html')
     return render(request,'search.html')