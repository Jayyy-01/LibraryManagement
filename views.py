from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from libraryapp.models import Author, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Author, Book

def add_author(request,auth = None):
    if request.method == 'POST':
        name = request.POST.get('Author')
        Author.objects.create(auth_name = name)
        auth = Author.objects.all()
        return render(request,'11.html',{'auth' : auth})
    return render(request,'1.html')

def info(request):
    auth = Author.objects.all()
    return render(request, '11.html', {'auth': auth})

def edit_auth(request,id):
    auth = Author.objects.get(id=id)
    if request.method == 'POST':
        auth.author = request.POST.get('Author')
        auth.save()
        return redirect('info')

def delete_auth(request,id):
    auth = Author.objects.get(id=id)
    auth.delete()
    return redirect('info')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'registration.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_aut')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
@user_passes_test(lambda u: u.is_superuser)

def insertauthor(request):
    if request.method == 'POST':
        auth_name = request.POST.get('auth_name')
        Author.objects.create(auth_name=auth_name)
        return HttpResponse('Author added successfully')
    return render(request,'Insertauthor.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def insertbook(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        auth = request.POST.get('auth_name')
        author = Author.objects.get(auth_name=auth)
        book_price = request.POST.get('book_price')
        Book.objects.create(book_name=book_name, author = author , book_price=book_price)
        return HttpResponse('Book added successfully')
    return render(request,'Insertbook.html')

@login_required
def bookauthor(request):
        author = Author.objects.all()
        book = Book.objects.all()
        di = {'aut':author,'boo':book}
        return render(request,'Book_Author.html',di)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def del_book(request, book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return redirect('book_aut')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_book(request,book_id):
    book = Book.objects.get(id = book_id)
    if request.method == 'POST':
        book.book_name = request.POST.get('book_name')
        auth_name = request.POST.get('auth_name')
        author = Author.objects.get(auth_name = auth_name)
        book.author = author
        book.book_price = request.POST.get('book_price')
        book.save()
        return redirect('book_aut')
    return render(request,'edit_book.html',{'book':book})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_author(request,auth_id):
    author = Author.objects.get(id = auth_id)
    if request.method == 'POST':
        author.auth_name = request.POST.get('auth_name')
        author.save()
        return redirect('book_aut')
    return render(request,'edit_author.html',{'author':author})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def del_author(request, auth_id):
    author = Author.objects.get(id = auth_id)
    author.delete()
    return redirect('book_aut')






