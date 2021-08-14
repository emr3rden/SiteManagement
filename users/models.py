from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from SiteManagement import settings



class CustomUser(AbstractUser):

    def __str__(self):
        return self.email



class Problems(models.Model):

    JOBS_CHOICES = (
        ('Elektrik', 'Elektrik Çalışanı'),
        ('Asansör', 'Asansör Çalışanı'),
        ('Bahçe', 'Bahçe Çalışanı'),
        ('Bina', 'Bina Çalışanı'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.CharField(max_length=100, choices=JOBS_CHOICES, verbose_name='İş Alanı')
    content = models.CharField(max_length=100, verbose_name='Sorun')
    published_date = models.DateTimeField(verbose_name='Oluşturulma Tarihi', auto_now_add=True)

    def publish(self):

        self.published_date = timezone.now()
        self.save()

    def __str__(self):

        return self.problem