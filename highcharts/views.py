from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.

def index(request):
	rendered = render_to_string('my_template.html', {'foo': 'bar'})
