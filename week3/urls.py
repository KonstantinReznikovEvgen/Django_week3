"""week3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobsite.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/<slug:pk>/', VacancyView.as_view(), name='vacancy'),
    path('vacancies/<slug:pk>/edit/', edit_view, name='edit'),
    path('vacancies/cat/<str:url_specialty>/', vacancies_specialization_view, name='vacancies_special'),
    path('companies/<int:company_pk>/', company_view, name='company'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('mycompanies/', my_companies_view, name='my_company_start'),
    path('mycompany/letsstart/', my_company_start, name='my_company_start'),
    path('mycompany/letsstart/create/<slug:pk>/', CompanyView.as_view(), name='my_company_create'),
    path('mycompany/letsstart/create/<slug:pk>/success/', success_view, name='success_view'),
    path('companies/<slug:pk>/edit', CompanyViewUpdate.as_view(), name='my_company_empty_form'),
    path('mycompany/vacancies/', my_vacancy, name='my_vacancy_start'),
    path('mycompany/vacancies/create/<slug:pk>/', MyVacanciesView.as_view(), name='my_vacancies_create'),
    path('mycompany/vacancies/create/<slug:pk>/success/', my_vacancy_success, name='my_vacancies_success'),
    path('login/', login.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


handler404 = custom_handler404
handler500 = custom_handler500
