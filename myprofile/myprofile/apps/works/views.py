from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from blog.models import Works

def Works_def(request):
	last_works = Works.objects.order_by('-pub_date')[:1]
	return render(request, 'blog/works.html', {'last_works': last_works})