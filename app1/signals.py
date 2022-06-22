import imp
from pyexpat import model
from django.db.models.signals import pre_delete, post_delete
from . models import MyModel
from django.dispatch import receiver
import os

@receiver(pre_delete, sender=MyModel)
def pre_del_fun(sender, **kwargs):
    print('pre delete fun')
    object = MyModel.objects.all()
    for data in object:
        if len(data.photo) > 0:
            os.remove(data.photo.path)
        break

@receiver(post_delete, sender=MyModel)
def post_del_fun(sender, **kwargs):
    print('post delete fun')
    object = MyModel.objects.all()
    for data in object:
        if len(data.photo) > 0:
            os.remove(data.photo.path)
        break