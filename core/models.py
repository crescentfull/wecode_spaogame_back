from django.db import models

class TimeStampedModel(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)
    deleted_at = models.DateTimeField(default=None, null=True)

    class Meta :
        abstract = True