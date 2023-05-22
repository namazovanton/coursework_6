from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserRoles, UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    USER_ROLES = [
        ("user", "Пользователь"),
        ("admin", "Администратор")
    ]
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = PhoneNumberField(max_length=12)
    email = models.EmailField(max_length=40, unique=True, null=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to="user_pics")

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role", "image"]

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin



