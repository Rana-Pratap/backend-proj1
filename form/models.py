from django.db import models


# Create your models here.
class Info(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    uname = models.CharField(max_length=35)
    addRe = models.TextField()
    cityn = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pinco = models.IntegerField()
    # check_me_out = models.BooleanField(null= True)

    def __str__(self):
        return self.fname

    class Meta:
        verbose_name_plural = "Info"

