from django.db import models
import uuid

class Template(models.Model):
    image = models.ImageField(upload_to='temp')
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

