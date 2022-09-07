from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# Create your models here.


# Create your models here.


class CONTACT(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    email = models.EmailField(("email"), max_length=254, null=False)
    subject = models.CharField(max_length=300, null=True)
    detail = models.TextField(null=False)

    def __str__(self):
        return self.email


class RESUME(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(("email"), max_length=254, null=False)
    resume = models.FileField(blank=False)

    def __str__(self):
        return self.email+self.name


class NOTICE(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=50, null=False)
    notice = models.FileField(blank=True)
    text = models.TextField(null=True)

    def __str__(self):
        return self.subject


class PYQS(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=200, null=False)
    note = models.TextField(null=True)
    question = models.FileField(blank=True)

    def __str__(self):
        return self.company
