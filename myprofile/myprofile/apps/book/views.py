from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from . models import Books

def index(request):
	books = Books.objects.all()
	return render(request, 'blog/books.html', {'books': books} )

