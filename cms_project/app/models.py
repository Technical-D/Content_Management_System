from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
# Create your models here.

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not any(char.islower() for char in password):
            raise ValidationError(_("The password must contain at least one lowercase letter."), code='password_no_lowercase')
        if not any(char.isupper() for char in password):
            raise ValidationError(_("The password must contain at least one uppercase letter."), code='password_no_uppercase')

    def get_help_text(self):
        return _(
            "Your password must contain at least one lowercase letter and one uppercase letter."
        )

class MyAuthorManager(BaseUserManager):
    def create_user(self, email ,full_name, phone,pincode, password):
        if not email:
            raise ValueError("User must have email address.")
        if not full_name:
            raise ValueError("Users must have a name")
        if not phone:
            raise ValueError("Users must have an phone no.")
        if not pincode:
            raise ValueError("Users must have pincode")

        user = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            phone = phone,
            pincode=pincode
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, full_name,pincode, phone, password):
        user = self.create_user(
            email = self.normalize_email(email),
            full_name = full_name,
            phone=phone,
            password = password,
            pincode=pincode #Default
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Author(AbstractBaseUser):
    full_name = models.CharField(verbose_name='name',max_length=30)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    phone = models.CharField(verbose_name='phone no', max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Field must be a 10-digit number')])
    address = models.CharField(verbose_name = 'address', blank=True, max_length=100)
    city = models.CharField(verbose_name = 'city', blank=True, max_length=50)
    state = models.CharField(verbose_name = 'state', blank=True, max_length=50)
    country = models.CharField(verbose_name = 'country', blank=True, max_length=50)
    pincode = models.CharField(max_length=6,validators=[RegexValidator(r'^\d{6}$', message='Field must be a 6-digit number')])
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_author = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','phone', 'pincode',]

    objects = MyAuthorManager()

    def __str__(self):
        return self.email
    
    # Checking for permission
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
