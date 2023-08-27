from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise TypeError('Email not')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


STATUS_CHOICE = (
    (1, _('Statussiz')),
    (2, _('Ishga tayyor')),
    (3, _('Band')),
)


class SubjectType(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=120)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Account(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=14, unique=True, db_index=True)
    username = models.CharField(max_length=222, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='accounts/')
    bio = models.TextField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_login = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user_status = models.IntegerField(choices=STATUS_CHOICE, default=1)
    is_pro = models.BooleanField(default=False)
    com_percent = models.PositiveSmallIntegerField(default=22)
    rating = models.PositiveIntegerField(default=0)
    specialist = models.ManyToManyField(Subject)

    objects = AccountManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone}'


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = _("Telefon raqamni tasdiqlash")
        verbose_name_plural = _("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name=_("Phone number"))
    code = models.CharField(max_length=10, verbose_name=_("Code"))

    def __str__(self):
        return self.phone
