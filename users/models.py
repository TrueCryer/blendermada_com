from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .data import COUNTRIES


class User(AbstractUser):

    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    send_newsletters = models.BooleanField(
        _('send newsletters'), default=False)

    send_notifications = models.BooleanField(
        _('send notifications'), default=False)

    country = models.CharField(_('country'),
        max_length=2,
        choices=COUNTRIES,
        default='RU',
    )

    show_fullname = models.BooleanField(
        _('show full name'), default=False)

    show_email = models.BooleanField(
        _('show e-mail'), default=False)

    about = models.TextField(_('about'), blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']