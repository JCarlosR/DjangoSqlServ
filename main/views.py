from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Planilla

def hello_world(request):
	planillas = Planilla.objects()
	template = loader.get_template('planillas.html')
	context = {
		'planillas': planillas
	}

	return HttpResponse(template.render(context, request))

# def developer(request, name):
# 	name=name.replace("_", " ")
# 	developer = Developer.objects(name=name).first()

# 	if request.method == 'POST':
# 		new_language = Language(name=request.POST['name'])
# 		developer.languages.append(new_language)
# 		developer.save()
# 		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/')) 

# 	template = loader.get_template('developer.html')
# 	context = {
# 		'developer': developer
# 	}

# 	return HttpResponse(template.render(context, request))

# def new_developer(request):
# 	if request.method == 'POST':
# 		new_developer = Developer(name=request.POST['name'], years=request.POST['years'], area=request.POST['area'])
# 		new_developer.save()
# 		return HttpResponseRedirect('/')

# 	areas = Area.objects()
# 	template = loader.get_template('register.html')
# 	context = {
# 		'areas': areas
# 	}

# 	return HttpResponse(template.render(context, request))	
