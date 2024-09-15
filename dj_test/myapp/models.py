from django.db import models
# Create your models here.

class TestModel(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name="Gambar")

    def __str__(self):
        return self.title

