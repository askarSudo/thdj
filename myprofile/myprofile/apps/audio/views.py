from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from blog.models import Works

def index(request):
	return render(request, 'blog/audio.html')