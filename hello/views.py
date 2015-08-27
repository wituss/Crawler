# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context

def index(request):
	template = loader.get_template('hello.html')
	hello = Context("foobar")
	return HttpResponse(template.render(hello))