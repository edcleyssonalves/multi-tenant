from django.contrib import admin
from .models import Company, CompanyUser


class CompanyUserInline(admin.TabularInline):
    model = CompanyUser
    extra = 1
    autocomplete_fields = ["user"]
    readonly_fields = []
    show_change_link = True


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")
    inlines = [CompanyUserInline]


@admin.register(CompanyUser)
class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "role")
    list_filter = ("company",)
    search_fields = ("user__username", "company__name")
