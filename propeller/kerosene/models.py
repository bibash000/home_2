from django.db import models

class uncle(models.Model):
    Relation = models.CharField(max_length=20)

    def __str__(self):
        return self.Relation 

class aunt(models.Model):
    commitment = models.CharField(max_length=20)
    choose = models.ManyToManyField(uncle,default='bibash')
    image = models.ImageField(upload_to='images',null=True,blank=True)
    def __str__(self):
        return self.commitment