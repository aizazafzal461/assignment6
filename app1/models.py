from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return '{1}'.format(instance, filename)

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    photo =  models.ImageField(upload_to = user_directory_path, blank=True)
