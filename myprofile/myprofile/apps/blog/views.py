from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from . models import Works, Hello_page

def index(request):
	hai = Hello_page.objects.all()
	return render(request, 'blog/main.html', {'hai': hai}, )

