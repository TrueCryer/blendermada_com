from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.urls import reverse


def get_filename(instance, filename):
    ext = Path(filename).suffix
    uuid = f'{uuid4()}'
    return Path('materials') / f'{uuid[0]}' / f'{uuid}' / f'{instance.slug}{ext}'


class Category(models.Model):

    name = models.CharField(_('name'), max_length=25)
    slug = models.SlugField(_('slug'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class MaterialManager(models.Manager):

    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(draft=False, **kwargs)


class Material(models.Model):

    ENGINES = (
        ('int', 'Blender Internal'),
        ('cyc', 'Cycles'),
        ('lux', 'Lux Render'),
        ('yfr', 'YafaRay'),
        ('oct', 'Octane'),
        ('nox', 'NOX Render'),
    )

    engine = models.CharField(_('render engine'), max_length=3, choices=ENGINES)
    category = models.ForeignKey(
        Category, related_name='materials', on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=20)
    slug = models.SlugField(_('slug'))
    description = models.TextField(_('description'), blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='materials',
        blank=True, null=True, on_delete=models.CASCADE,
    )
    date = models.DateTimeField(_('date'), default=timezone.now)
    draft = models.BooleanField(_('draft'), default=True)
    library = models.FileField(
        _('library'), upload_to=get_filename, blank=True
    )
    preview = models.ImageField(
        _('preview'), upload_to=get_filename, blank=True
    )

    objects = MaterialManager()

    class Meta:
        verbose_name = _('material')
        verbose_name_plural = _('materials')
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('materials:detail', kwargs={'pk': self.pk, 'slug': self.slug})
    
    def __str__(self):
        return f"{self.category} - {self.name}"