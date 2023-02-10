from .models import Uzduotis
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from .forms import UserUzduotisCreateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)


# Create your views here.

def index(request):
    num_uzduotis = Uzduotis.objects.all().count()

    context = {
        'num_uzduotis': num_uzduotis,
    }
    return render(request, 'index.html', context=context)


class UserUzduotysListView(LoginRequiredMixin, generic.ListView):
    model = Uzduotis
    template_name = 'vartotojo_uzduotis.html'

    def get_queryset(self):
        return Uzduotis.objects.filter(vartotojas=self.request.user).order_by('sukurta')


class UzduotisListView(generic.ListView):
    model = Uzduotis
    template_name = 'uzduotis_list.html'


class UzduotisDetailView(generic.DetailView):
    model = Uzduotis
    template_name = 'uzduotis_detail.html'


def form_valid(self, form):
    form.instance.uzduotis = self.object
    form.instance.vartotojas = self.request.user
    form.save()
    return super(UzduotisDetailView, self).form_valid(form)


class UserUzduotisCreateView(LoginRequiredMixin, CreateView):
    model = Uzduotis
    success_url = "/planavimoappsas/vartotojo_uzduotis/"
    template_name = 'vartotojo_uzduotis_form.html'
    form_class = UserUzduotisCreateForm

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        return super().form_valid(form)


class UserUzduotisUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Uzduotis
    fields = ['uzduotis', 'sukurta']
    success_url = "/planavimoappsas/vartotojo_uzduotis/"
    template_name = 'vartotojo_uzduotis_form.html'

    def form_valid(self, form):
        form.instance.vartotojas = self.request.user
        return super().form_valid(form)

    def test_func(self):
        uzduotis = self.get_object()
        return self.request.user == uzduotis.vartotojas


class UserUzduotisDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Uzduotis
    success_url = "/planavimoappsas/vartotojo_uzduotis/"
    template_name = 'vartotojo_uzduotis_delete.html'

    def test_func(self):
        uzduotis = self.get_object()
        return self.request.user == uzduotis.vartotojas


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')
