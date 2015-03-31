from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20, blank=False)
    code = models.TextField()
    user = models.ForeignKey(User, related_name="snippets_of_user")

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return u'{}'.format(self.title)
