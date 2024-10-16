from django.contrib import admin
from educational_course import models
# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','surname')
@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)
@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(models.Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('date_of_purchase',)
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email',)

