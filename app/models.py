from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    network= models.CharField(max_length=255)
    date= models.DateField()
    desc = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
                return f'{self.title} {self.desc}'

    def __str__(self):
                return f'{self.title} {self.desc}'                          