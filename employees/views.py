from django.shortcuts import render
from django.http import HttpResponse
from employees.models import employees_db

# Create your views here.
def employees_page(request):
	# data = {}
	# passing single variable
	# data["name"] = 'Prathamesh'

	# fetching data from models
	dbData = {"data" : employees_db.objects.all()}

	return render(request, 'index.html',dbData)