from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # Extra Infomation - This Class is Abstract Model
    class Meta:
        abstract = True
