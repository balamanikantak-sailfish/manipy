from django.http import HttpResponse
from django.template import loader
	
	
def index(request):
    template = loader.get_template('dashboard.html')
    context = {
        'data': 'index',
    }
    return HttpResponse(template.render(context, request))