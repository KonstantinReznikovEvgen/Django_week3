from django.contrib import admin
from jobsite.models import Vacancy, Company, Application, Specialty

# Register your models here.

class VacancyAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

class ApplicationAdmin(admin.ModelAdmin):
    pass

class SpecialtyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Specialty,SpecialtyAdmin)
