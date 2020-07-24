"""
Models: Cuty, Language, Vacancy
"""

from django.db import models
from scraping.utils import transletition


class City(models.Model):
    """
    Model City, fields: name, slug
    """
    name = models.CharField(max_length=100,
                            verbose_name='Name of City',
                            unique=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Name of City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        Переопределяем save
        В документации django при переопредлении метода в него передается *args, **kwargs
        Преобразуем с помощью transletition название города в слаг
        """
        if not self.slug:
            self.slug = transletition(str(self.name))
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)


class Language(models.Model):
    """
    Model Language, fields: name, slug
    """
    name = models.CharField(max_length=100,
                            verbose_name='Programming Language',
                            unique=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Programming Language'
        verbose_name_plural = 'Programming Languages'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        Переопределяем save
        В документации django при переопредлении метода в него передается *args, **kwargs
        Преобразуем с помощью transletition название города в слаг
        """
        if not self.slug:
            self.slug = transletition(str(self.name))
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)


class Vacancy(models.Model):
    """
    Model Language, fields: url, title, company, description, timestamp
    "one-to-many" fields: city, language
    """
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Vacancy')
    company = models.CharField(max_length=250, verbose_name='Company')
    description = models.TextField(verbose_name='About')
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, verbose_name='Name of City')
    language = models.ForeignKey(
        'Language', on_delete=models.CASCADE, verbose_name='Programming Language')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title

    def short(self):
        """
        Метод возвращает короткое description
        """
        return self.description[:100]
