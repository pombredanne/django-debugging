from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    """
from snippets.models import Snippet
import random
u_id = random.randint(1,3)

for i in range(1,300):
    Snippet.objects.create(title="title%s" % i, user_id=u_id)

    """

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20, blank=False)
    code = models.TextField()
    user = models.ForeignKey(User, related_name="snippets_of_user")

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return u'{}'.format(self.title)
