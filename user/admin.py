from django.contrib import admin
from .models import Account, Subject, SubjectType, VerifyPhone

admin.site.register(Account)
admin.site.register(Subject)
admin.site.register(SubjectType)
admin.site.register(VerifyPhone)
