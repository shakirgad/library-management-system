from django.shortcuts import render,redirect
from .models import *
from .forms import  BookForm, CatForm



# Create your views here.
def index(request):
    
    if request.method == 'POST':
        add_book = BookForm(request.POST)
        if add_book.is_valid():
           add_book.save()
     
    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
        'form':BookForm(),
        'catform':CatForm(),
        'all_books': Book.objects.filter(active=True).count(),
    }
    return render(request,'pages/index.html',context)
    
    
def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET :
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains= title)
               
    context = {
        'category': Category.objects.all(),
        'books':search,
        
    }
    

    return render(request,'pages/books.html',context) 
    
    
def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST' :
       up_form = BookForm(request.POST,instance = book_id)
       if up_form.is_valid():
          up_form.save()
          return redirect('/')
    else:
        up_form = BookForm(instance = book_id) 
        
    context = {
        'update_form':up_form,
    }
        
    return render(request,'pages/update.html',context)
    
    
        
def delete(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
    
