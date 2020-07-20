from django.db import models

from scraping.utils import transletition


class City(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Name of City',
                            unique=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Name of City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Переопределяем def save
        Преобразуем с помощью def transletition название города в слаг
        """
        if not self.slug:
            self.slug = transletition(str(self.name))
        super().save(*args, **kwargs)    


class Language(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Programming Language',
                            unique=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Programming Language'
        verbose_name_plural = 'Programming Languages'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Переопределяем def save
        Преобразуем с помощью def transletition название города в слаг
        """
        if not self.slug:
            self.slug = transletition(str(self.name))
        super().save(*args, **kwargs)
