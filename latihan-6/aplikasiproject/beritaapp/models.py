from django.db import models

# Create your models here.
# declare a new model with a name "GeeksModel"
class BeritaModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200, default='Author')
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title