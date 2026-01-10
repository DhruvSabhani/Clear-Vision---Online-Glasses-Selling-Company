from django.db import models

# Create your models here.
class UserAdmin(models.Model):
    admin_id = models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='Admin ID')
    username = models.CharField(max_length=255,blank=True,null=True,verbose_name='Username')
    email = models.EmailField(verbose_name='Email ID',blank=True)
    password = models.CharField(max_length=255,blank=True,verbose_name='Passwors')
    joind_date = models.DateField(verbose_name='Joind Date',null=True,blank=True)
    joind_time = models.TimeField(verbose_name='Joind Time',blank=True,null=True)
    def __str__(self):
        return self.email