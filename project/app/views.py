from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, UserForm2
from .models import Person



def getData(request):
    tom = Person.objects.update_or_create(name="Tom2", age=26, photo='bbv.jpg')
    try:
        men = Person.objects.get(name='Mike2')
    except ObjectDoesNotExist:
        str = 'Not found'
    # if not men:
    #     mike = Person(name="Mike", age=15, photo='gdfgs.jpg')
    #     mike.save()
    people = Person.objects.filter(name='Tom2').exclude
    return render(request, 'app/data.html', context={'data': people, 'str': str})



def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            return redirect('home')
        else:
            return HttpResponse('Данные не валидны')
    else:
        form = UserForm()
        form2 = UserForm2()
        return render(request, 'app/index.html', context={'form': form, 'form2': form2})