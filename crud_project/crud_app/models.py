from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    write = models.CharField(max_length=20)
    body = models.TextField()
    pud_date= models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]