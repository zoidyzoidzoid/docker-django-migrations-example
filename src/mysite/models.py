from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Owner(BaseModel):
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Pet(BaseModel):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128, default='Dog')
    owner = models.ForeignKey('Owner')
