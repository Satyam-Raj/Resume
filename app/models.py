from django.db import models
from django.contrib.auth.models import User



                            # from here these classes are for profile edit section:


class Professional(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    



    First_Name          =                    models.CharField(max_length=14,null=True)
    Last_Name           =                    models.CharField(max_length=14,null=True)
    Date_of_Birth       =                    models.CharField(max_length=12,null=True)
    

    Mobile_Number       =                    models.CharField(max_length=10,null=True)
    Email               =                    models.CharField(max_length=80,null=True)
    
    Country             =                    models.CharField(max_length=20,null=True)
    State               =                    models.CharField(max_length=20,null=True)
    City                =                    models.CharField(max_length=20,null=True)
    Regional_place      =                    models.CharField(max_length=20,null=True)



    
    Introduction                 =       models.TextField(null=True)


    Job_Title                    =       models.CharField(max_length=30,null=True, blank=True)
    Company_Name                 =       models.CharField(max_length=30,null=True, blank=True)
    Locaton                      =       models.CharField(max_length=30,null=True, blank=True)
    Duration                     =       models.CharField(max_length=20,null=True, blank=True)

    Description                  =       models.TextField(blank=True) 


    
    First_Experience_Job_Title                           =       models.CharField(max_length=30,null=True, blank=True)
    First_Exp_Company_Name                        =       models.CharField(max_length=30,null=True, blank=True)
    First_Exp_Company_Location                    =       models.CharField(max_length=30,null=True, blank=True)
    First_Exp_Company_Duration                    =       models.CharField(max_length=20,null=True, blank=True)

    First_Experience_Description                         =       models.TextField(blank=True)





    Second_Experience_Job_Title                           =       models.CharField(max_length=30,null=True, blank=True)
    Second_Exp_Company_Name                        =       models.CharField(max_length=30,null=True, blank=True)
    Second_Exp_Company_Location                    =       models.CharField(max_length=30,null=True, blank=True)
    Second_Exp_Company_Duration                    =       models.CharField(max_length=20,null=True, blank=True)

    Second_Experience_Description                         =       models.TextField(blank=True)





    Third_Experience_Job_Title                           =       models.CharField(max_length=30,null=True, blank=True)
    Third_Exp_Company_Name                        =       models.CharField(max_length=30,null=True, blank=True)
    Third_Exp_Company_Location                    =       models.CharField(max_length=30,null=True, blank=True)
    Third_Exp_Company_Duration                    =       models.CharField(max_length=20,null=True, blank=True)

    Third_Experience_Description                         =       models.TextField(blank=True)





    Fourth_Experience_Job_Title                           =       models.CharField(max_length=30,null=True, blank=True)
    Fourth_Exp_Company_Name                        =       models.CharField(max_length=30,null=True, blank=True)
    Fourth_Exp_Company_Location                    =       models.CharField(max_length=30,null=True, blank=True)
    Fourth_Exp_Company_Duration                    =       models.CharField(max_length=20,null=True, blank=True)

    Fourth_Experience_Description                         =       models.TextField(blank=True)






    Fifth_Experience_Job_Title                           =       models.CharField(max_length=30,null=True, blank=True)
    Fifth_Exp_Company_Name                        =       models.CharField(max_length=30,null=True, blank=True)
    Fifth_Exp_Company_Location                    =       models.CharField(max_length=30,null=True, blank=True)
    Fifth_Exp_Company_Duration                    =       models.CharField(max_length=20,null=True, blank=True)

    Fifth_Experience_Description                         =       models.TextField(blank=True)








    Board                            =               models.CharField(max_length = 10,null=True)
    School_Name                      =               models.CharField(max_length = 40,null=True)
    School_Location                  =               models.CharField(max_length = 30,null=True)
    School_Duration                  =               models.CharField(max_length = 20,null=True)

    School_Description               =               models.TextField(null=True)




    Specialization                            =               models.CharField(max_length = 20,null=True)
    College_Name                      =               models.CharField(max_length = 40,null=True)
    College_Location                  =               models.CharField(max_length = 30,null=True)
    College_Duration                  =               models.CharField(max_length = 20,null=True)

    College_Description              =               models.TextField(null=True)




    First_Skill_category         =       models.CharField(max_length=25, null=True)
    First_Skill                  =       models.CharField(max_length=80, null=True)


    Second_Skill_category         =       models.CharField(max_length=25,null=True, blank=True)
    Second_Skill                  =       models.CharField(max_length=80,null=True, blank=True)


    Third_Skill_category         =       models.CharField(max_length=25,null=True, blank=True)
    Third_Skill                    =       models.CharField(max_length=80,null=True, blank=True)


    Fourth_Skill_category         =       models.CharField(max_length=25,null=True, blank=True)
    Fourth_Skill                  =       models.CharField(max_length=80,null=True, blank=True)


    Fifth_Skill_category         =       models.CharField(max_length=25,null=True, blank=True)
    Fifth_Skill                  =       models.CharField(max_length=80,null=True, blank=True)


    # Sixth_Skill         =       models.CharField(max_length=120, blank=True)
    # Seventh_Skill        =       models.CharField(max_length =120, blank=True)
    



    First_Language       =       models.CharField(max_length=80,null=True)
    Second_Language       =       models.CharField(max_length=80,null=True, blank=True)
    Third_Language       =       models.CharField(max_length=80,null=True, blank=True)
    Fourth_Language       =       models.CharField(max_length=80,null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'



class Contact(models.Model):
    
    Name                             = models.CharField(max_length=120)
    Email                            = models.EmailField(max_length=120)
    Professional_Status              = models.CharField(max_length=100)             #  this class is for 'Contact Us' page
    Country                          = models.CharField(max_length=100)
    How_you_came_to_know_about_us    = models.CharField(max_length=250)
    Message                          = models.TextField()
