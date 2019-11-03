from django.db import models


class Conference(models.Model):
    name = models.CharField(max_length=50)
    admin_email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

