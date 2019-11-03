from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from blog.models import Program

def Program_def(request):
	last_program = Program.objects.order_by('-pub_date')[:5]
	return render(request, 'blog/prog.html', {'last_program': last_program})