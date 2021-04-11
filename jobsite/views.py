from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from jobsite.models import Vacancy, Company, Specialty, Application
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from jobsite.forms import *
from django.views.generic import DetailView, UpdateView


dict_of_specialties = {
    'frontend': "Фронтенд",
    'backend': "Бэкенд",
    'devops': "Девопс",
    'gamedev': "Геймдев",
    'design': "Дизайн",
    'management': "Менеджмент",
    'testing': "Тестирование",
    'products': "Продукты"
}


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы нет.')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера! Вероятно, такого ключа нет!')


def main_view(request):
    return render(request, 'jobsite/index.html', context={
        'specialties': Specialty.objects.all(),
        'companies': Company.objects.all()
    }
                  )


def vacancies_view(request):
    return render(request, 'jobsite/vacancies.html', context={
        'vacancies': Vacancy.objects.all()
    }
                  )


def vacancies_specialization_view(request, url_specialty):
    context = {
        "specialty": dict_of_specialties[url_specialty],
        "url_vacancies": Vacancy.objects.filter(specialty__code=url_specialty)
    }
    return render(request, 'jobsite/particular_vacancy.html', context=context)


def company_view(request, company_pk):
    return render(request, 'jobsite/my-company.html', context={
        'company': Company.objects.get(id=company_pk),
        'vacancies': Vacancy.objects.filter(company__id=company_pk),
        'company_pk': company_pk
    }
                  )


def vacancy_view(request, vacancy_pk):
    return render(request, 'jobsite/vacancy.html', context={
        'vacancy': Vacancy.objects.get(id=vacancy_pk)
    }
                  )


class VacancyView(DetailView):
    model=Vacancy
    template_name = "jobsite/vacancy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResponseForm
        return context

    def post(self, request, pk):
        form = ResponseForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user_id = request.user.pk
            application.vacancy_id = pk
            application.save()
            return HttpResponseRedirect('edit/')
        self.object = self.get_object()
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class CompanyViewUpdate(UpdateView):
    model=Company
    template_name = "jobsite/company-edit.html"
    form_class = CompanyForm
    success_url = 'success_update/'

    def update(self, request, pk):
        form = CompanyForm(request.POST)
        if request.method:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('success_update/')
        return render(request, 'jobsite/index.html', {'form': form})


class MyVacanciesView(DetailView):
    model=Vacancy
    template_name = "jobsite/vacancy-edit.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VacancyForm
        return context

    def post(self, request, pk):
        form = VacancyForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy_id = pk
            application.user= request.user
            application.save()
            return HttpResponseRedirect('success/')
        self.object = self.get_object()
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)



class CompanyView(DetailView):
    model=Company
    template_name = "jobsite/company-edit.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CompanyForm
        return context

    def post(self, request, pk):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.owner_id = request.user.pk
            application.company_id = pk
            application.save()
            return HttpResponseRedirect('success/')
        self.object = self.get_object()
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

def my_vacancy_list(request):
    return render(request, 'jobsite/my-vacancies.html')


def my_vacancy(request):
    return render(request, 'jobsite/my-vacancy.html')

def my_vacancy_success(request, pk):
    return render(request, 'jobsite/Success_create_vacancy.html')

def success_view(request, pk):
    return render(request, 'jobsite/Success_create.html')

def edit_view(request,pk):
    return render(request, 'jobsite/send-application.html')

def my_company_start(request):
    return render(request, 'jobsite/create-company.html', context={

    }
                  )


def my_companies_view(request):
    return render(request, 'jobsite/my-company.html', context={

    }
                  )



class login(LoginView):
    redirect_authenticated_user = True
    template_name = 'login-logout.html'


def register(request):
   if request.method == "POST":
       form = UserForm(request.POST)
       if form.is_valid():
           new_user= User.objects.create_user(**form.cleaned_data)
           login(new_user)
           form.save()
           return HttpResponseRedirect('index.html')
   else:
       form=UserForm()

   return render(request, 'register.html', context={
      'form': form
  }
                )



def logout(request):
    return render(request, 'jobsite/login-logout.html', context={

    }
                  )
