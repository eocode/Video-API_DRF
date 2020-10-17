from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title = models.CharField(_("Title"), max_length=50, blank=True, null=True)
    description = models.TextField(_("Description"), max_length=50)
    slug = models.SlugField(_("Slug"), max_length=50)
    created_at = models.DateTimeField(
        _("Created at"), auto_now=True, auto_now_add=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title