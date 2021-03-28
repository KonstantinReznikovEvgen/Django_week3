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
from jobsite.views import main_view, vacancy_view, vacancies_specialization_view, \
    company_view, vacancies_view, custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/<int:vacancy_pk>/', vacancy_view, name='vacancy'),
    path('vacancies/cat/<str:url_specialty>/', vacancies_specialization_view, name='vacancies_special'),
    path('companies/<int:company_pk>/', company_view, name='company'),
    path('vacancies/', vacancies_view, name='vacancies'),
]
handler404 = custom_handler404
handler500 = custom_handler500
