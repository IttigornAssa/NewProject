from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import PersonForm
from .models import Person
from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector

def home(request):
	return render(request,'home.html')

def listPerson(request):
	queryset = Person.objects.all()

	query = request.GET.get('q')
	if query:
		queryset = queryset.annotate(
			search=SearchVector('name','author','abstract'),
		).filter(search=query)
		# queryset = queryset.filter(
		# 	Q(name__icontains = query) | 
		# 	Q(department__icontains = query)
		# 	).distinct()

	context = {
		'object_list':queryset,
	}
	return render(request, 'home.html',context)

def model_form_upload(request):
	
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })



# def home(request):
# 	return render(request, 'home.html', {'key': "value" })

# class CreatePersonView(CreateView):
# 	queryset = Person()
# 	template_name='person.html'
# 	form_class = PersonForm
# 	success_url = '/'

# class UpdatePersonView(UpdateView):
# 	queryset = Person.objects.all()
# 	template_name='person.html'
# 	form_class = PersonForm
# 	success_url = '/'

# class ListPersonView(ListView):
#     model = Person
#     template_name='person_list.html'


# class Home2(ListView):
#     model = Person
#     template_name='home.html'

       