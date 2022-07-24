from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Management(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class SubstituteDirector(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.TextField()
    management = models.ForeignKey(Management, on_delete=models.CASCADE)
    substituteDirector = models.ForeignKey(SubstituteDirector, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    pos = [
        ('yetakchi', 'yetakchi mutaxasis'),
        ('bosh', 'bosh mutaxasis'),
        ('bolim boshliq', 'bolim boshliq'),
        ('BB', 'boshqarma boshliq'),
        ('DO', 'direktor ornbosar'),
        ('D', 'direktor'),
    ]
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    position = models.CharField(max_length=50, choices=pos, default='yetakchi')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)


class Xodim(models.Model):
    NEW = 'Yangi hujjat yaratish'
    ijro_intizom = 'Ijro intizomi'
    yillik = 'Yillik ish rejasi ijrosi'
    ijodiy = 'Ijodiy faoliyat'
    tashabbus = 'Tashabbuskorlik'
    mehnat = 'Mehnat intizomi'
    PROJECT_STATUS_CHOICES = (
        (NEW, 'Yangi hujjat yaratish'),
        (ijro_intizom, 'Ijro intizomi'),
        (yillik, 'Yillik ish rejasi ijrosi'),
        (ijodiy, 'Ijodiy faoliyat'),
        (tashabbus, 'Tashabbuskorlik'),
        (mehnat, 'Mehnat intizomi'),
    )
    archiveStatus = [
        ('0', '0'),
        ('1', '1'),
    ]
    type_doc = models.CharField(max_length=50, choices=PROJECT_STATUS_CHOICES)
    description = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    submit_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_kpi_doc/')
    status = models.CharField(max_length=25, choices=archiveStatus, default='0')
    score = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.user} {self.type_doc}"

    def get_absolute_url(self):
        return reverse('mydoc')
