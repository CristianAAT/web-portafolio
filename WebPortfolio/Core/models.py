from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project (models.Model):
    name = models.CharField(
        verbose_name='Project Name',
        max_length=20
    )
    description = RichTextField(
        verbose_name='Description'
    )
    link = models.URLField(
        verbose_name='Link',
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add= True,
        verbose_name= 'Fecha de creación'
    )
    updated = models.DateTimeField(
        auto_now= True,
        verbose_name= 'Fecha de actualización'
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['name']

    def __str__(self):
        return self.name