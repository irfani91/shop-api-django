from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import City
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello_view(request):
    html = '<html><body><p>Belajar Django.</p></body></html>'
    return HttpResponse(html)

@login_required
def city_list_view(request, state_id):
    cities = City.objects.filter(state=state_id)
    return JsonResponse({'data': [{'id': city.id, 'name': city.name} for city in cities]})
