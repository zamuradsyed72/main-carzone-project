from django.db import models
 
# Create your models here.
class Team (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook_link = models.URLField(max_length=255)
    google_link = models.URLField(max_length=255)
    # twitter_link = models.URLField(max_length=255)
    created_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.first_name
    
   