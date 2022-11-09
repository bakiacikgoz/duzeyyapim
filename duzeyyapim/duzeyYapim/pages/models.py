from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length = 100, verbose_name = "Adı ve Soyadı")
    email = models.EmailField(max_length = 100, verbose_name = "E-Mail")
    phone = models.CharField(max_length = 100, verbose_name = "Telefon Numarası")
    dept = models.CharField(max_length = 100, verbose_name = "Departman")
    message = models.TextField(blank=True , verbose_name = "Mesaj")
    ileti_tarihi =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Gelen Formlar"

    def __str__(self):
        return self.email
