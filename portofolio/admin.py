from django.contrib import admin
from portofolio import models
# Register your models here.
admin.site.register(models.PersonalInformation)
admin.site.register(models.About)
admin.site.register(models.Project)
admin.site.register(models.Contact)