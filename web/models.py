from django.db import models

# Create your models here.

class TodoListItem(models.Model):
    content = models.TextField() 
    id = models.BigAutoField(primary_key=True)
    class Meta:
        ordering=('id',)