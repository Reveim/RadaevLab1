from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.views import View

from .forms import UserCreationForm, AddExcursionForm
from .models import Excursion
from django.views.generic import DetailView, CreateView


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def excursions(request):
    exc = Excursion.objects.all()
    return render(request, 'main/excursion.html', {'exc': exc, })

class ExcursionDetailView(DetailView):
    model = Excursion
    template_name = 'main/detail_excursion.html'
    context_object_name = 'excursion'

class AddExcursion(CreateView):
    form_class = AddExcursionForm
    template_name = 'main/add_excursion.html'


def gallery(request):
    pics = Excursion.objects.all()
    return render(request, 'main/gallery.html', {'pics': pics})

def contacts(request):
    return render(request, 'main/contacts.html')

#@login_required
#def profile_view(request):
#    return render(request, 'main/profile.html')

class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context ={
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password )
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
