from django.contrib import admin

# Register your models here.
from officeaccounts.models import Account,Transaction

admin.site.register(Account)
admin.site.register(Transaction)