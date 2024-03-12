from django.db import models

# Create your models here.
class blog(models.Model):
    image=models.ImageField(upload_to='blog',blank=True,null=True)
    title =models.CharField(max_length=25)
    description=models.TextField()
    date=models.DateField((""), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
