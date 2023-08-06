from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
import uuid


class UserManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, username, role, password=None):
        user = self.model(firstname=firstname, lastname=lastname,
                          email=self.normalize_email(email),
                          username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, firstname, lastname, email, role, username,
                         password=None):
        user = self.model(firstname=firstname, lastname=lastname,
                          email=self.normalize_email(email),
                          username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_verified = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    public_key = models.UUIDField(default=uuid.uuid4, editable=False,
                                  null=False, unique=True)
    email = models.EmailField(max_length=50, unique=True, null=False)
    username = models.CharField(max_length=50, null=False)
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    is_verified = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        ordering = ['-id']
