from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.name


class CompanyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_user')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users')
    role = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.company.name}'
