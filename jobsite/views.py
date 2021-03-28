from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from jobsite.models import Vacancy, Company, Specialty


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
        'specialties': Specialty.objects.filter(code__in=['backend', 'frontend']),
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
    return render(request, 'jobsite/company.html', context={
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
