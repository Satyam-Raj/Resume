from django.db import models
from django.contrib.auth.models import User



                            # from here these classes are for profile edit section:


class Professional(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    



    First_Name          =                    models.CharField(max_length=14,null=True)
    Last_Name           =                    models.CharField(max_length=14,null=True)
    Date_of_Birth                 =                    models.CharField(max_length=12,null=True)
    

    Mobile_Number       =                    models.CharField(max_length=10,null=True)
    Email               =                    models.CharField(max_length=80,null=True)
    Address             =                    models.CharField(max_length=80,null=True)


    
    Introduction                 =       models.TextField(null=True)
    Currently_or_was_working_for =       models.CharField(max_length=115, blank=True)
    Description                  =       models.TextField(blank=True) 


    First_Experience                                     =       models.CharField(max_length=126, blank=True)
    First_Experience_Description                         =       models.TextField(blank=True)

    Second_Experience                                     =       models.CharField(max_length=126, blank=True)
    Second_Experience_Description                         =       models.TextField(blank=True)

    Third_Experience                                     =       models.CharField(max_length=126, blank=True)
    Third_Experience_Description                         =       models.TextField(blank=True)

    Fourth_Experience                                     =       models.CharField(max_length=126, blank=True)
    Fourth_Experience_Description                         =       models.TextField(blank=True)

    Fifth_Experience                                     =       models.CharField(max_length=126, blank=True)
    Fifth_Experience_Description                         =       models.TextField(blank=True)




    School                  =               models.CharField(max_length = 126,null=True)
    School_Description      =               models.TextField(null=True)

    College                 =               models.CharField(max_length = 126,null=True)
    College_Description     =               models.TextField(null=True)


    First_Skill         =       models.CharField(max_length=120,null=True)
    Second_Skill        =       models.CharField(max_length =120,null=True)
    Third_Skill        =       models.CharField(max_length =120,null=True)
    Fourth_Skill         =       models.CharField(max_length=120, blank=True)
    Fifth_Skill        =       models.CharField(max_length =120, blank=True)
    Sixth_Skill         =       models.CharField(max_length=120, blank=True)
    Seventh_Skill        =       models.CharField(max_length =120, blank=True)
    

    Fist_Language       =       models.CharField(max_length=112,null=True)
    Second_Language       =       models.CharField(max_length=112, blank=True)
    Third_Language       =       models.CharField(max_length=112, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'



class Contact(models.Model):
    
    Name                             = models.CharField(max_length=120)
    Email                            = models.EmailField(max_length=120)
    Professional_Status              = models.CharField(max_length=100)             #  this class is for 'Contact Us' page
    Country                          = models.CharField(max_length=100)
    How_you_came_to_know_about_us    = models.CharField(max_length=250)
    Message                          = models.TextField()
