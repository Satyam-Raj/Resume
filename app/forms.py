from django import forms
from .models import Professional, Contact


class Profile_update_form(forms.ModelForm):
    class Meta:
        model = Professional
        fields = [
            'image',
            'First_Name',
            'Last_Name',
            'Date_of_Birth',

            'Mobile_Number',
            'Email',

            'Country',
            'State',
            'City',
            'Regional_place',

           
            'Introduction',

            'Job_Title',
            'Company_Name',
            'Locaton',
            'Duration',

            'Description',


            'First_Experience_Job_Title',
            'First_Exp_Company_Name',
            'First_Exp_Company_Location',
            'First_Exp_Company_Duration',

            'First_Experience_Description',


            'Second_Experience_Job_Title',
            'Second_Exp_Company_Name',
            'Second_Exp_Company_Location',
            'Second_Exp_Company_Duration',

            'Second_Experience_Description',



            'Third_Experience_Job_Title',
            'Third_Exp_Company_Name',
            'Third_Exp_Company_Location',
            'Third_Exp_Company_Duration',

            'Third_Experience_Description',



            'Fourth_Experience_Job_Title',
            'Fourth_Exp_Company_Name',
            'Fourth_Exp_Company_Location',
            'Fourth_Exp_Company_Duration',

            'Fourth_Experience_Description',



            'Fifth_Experience_Job_Title',
            'Fifth_Exp_Company_Name',
            'Fifth_Exp_Company_Location',
            'Fifth_Exp_Company_Duration',

            'Fifth_Experience_Description',



            'Board',
            'School_Name',
            'School_Location',
            'School_Duration',

            'School_Description',



            'Specialization',
            'College_Name',
            'College_Location',
            'College_Duration',

            'College_Description',



           'First_Skill_category',
           'First_Skill',


           'Second_Skill_category',
           'Second_Skill',


           'Third_Skill_category',
           'Third_Skill',


           'Fourth_Skill_category',
           'Fourth_Skill',

           'Fifth_Skill_category',
           'Fifth_Skill',


        #    'Sixth_Skill',
        #    'Seventh_Skill',



           'First_Language',
           'Second_Language',
           'Third_Language',
           'Fourth_Language',

        ]



        widgets = {

            

            'First_Name'                         :          forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your First Name','onfocus': 'this.placeholder = ''','onblur': "this.placeholder = 'About Your organization'",}),
            'Last_Name'                          :          forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Last Name'}),
            'Date_of_Birth'                      :          forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Date of Birth'}),

            'Mobile_Number'                     :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your mobile number'}),
            'Email'                             :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your email'}),


            'Country'                               :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}),
            'State'                                 :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'City'                                    :           forms.TextInput(attrs={'class':'form-control', 'placeholder':' City'}),
            'Regional_place'                           :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Regional place'}),



            'Introduction'                      :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Introduce yourself','maxlength': '600'}),
          
            'Job_Title'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title (Optional field)'}),
            'Company_Name'                        :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Name (Optional)'}),
            'Locaton'                             :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location (Optional field)'}),
            'Duration'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration (Optional field)'}),
           
            'Description'                       :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'It is ok to brag about your desingnation, promotions and achievements (This field is optional)', 'maxlength': '900',}),


            'First_Experience_Job_Title'                                    :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title (Optional field)'}),
            'First_Exp_Company_Name'                                 :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Name (Optional)'}),
            'First_Exp_Company_Location'                             :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location (Optional field)'}),
            'First_Exp_Company_Duration'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration (Optional field)'}),
           
            
            'First_Experience_Description'      :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),
            
            
            
            'Second_Experience_Job_Title'                                    :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title (Optional field)'}),
            'Second_Exp_Company_Name'                                :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Name (Optional)'}),
            'Second_Exp_Company_Location'                             :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location (Optional field)'}),
            'Second_Exp_Company_Duration'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration (Optional field)'}),
           
            
            'Second_Experience_Description'     :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),

           
           
            'Third_Experience_Job_Title'                                 :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title (Optional field)'}),
            'Third_Exp_Company_Name'                              :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Name (Optional)'}),
            'Third_Exp_Company_Location'                             :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location (Optional field)'}),
            'Third_Exp_Company_Duration'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration (Optional field)'}),
           
            
            'Third_Experience_Description'      :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),

           
           
            'Fourth_Experience_Job_Title'                                      :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title (Optional field)'}),
            'Fourth_Exp_Company_Name'                                 :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Name (Optional)'}),
            'Fourth_Exp_Company_Location'                             :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location (Optional field)'}),
            'Fourth_Exp_Company_Duration'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration (Optional field)'}),
           
           
            'Fourth_Experience_Description'     :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),

           
           
            'Fifth_Experience_Job_Title'                                     :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title (Optional field)'}),
            'Fifth_Exp_Company_Name'                                 :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Name (Optional)'}),
            'Fifth_Exp_Company_Location'                             :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location (Optional field)'}),
            'Fifth_Exp_Company_Duration'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration (Optional field)'}),
           
            
            'Fifth_Experience_Description'      :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),


           
           
            'Board'                                     :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your school Board'}),
            'School_Name'                                 :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'School Name'}),
            'School_Location'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'School Location'}),
            'School_Duration'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration'}),
            
            'School_Description'                :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description','maxlength': '400'}),

            
            
            'Specialization'                           :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Specialization'}),
            'College_Name'                           :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'College Name'}),
            'College_Location'                           :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'College Location'}),
            'College_Duration'                           :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duration'}),
            
            'College_Description'               :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description','maxlength': '500'}),


           
            'First_Skill_category'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}),
            'First_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill | Skill | Skill'}),
            
            
            'Second_Skill_category'                      :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category (Optional field)'}),
            'Second_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill | Skill | Skill (Optional field)'}),
           
           
            'Third_Skill_category'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category (Optional field)'}),
            'Third_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill | Skill | Skill (Optional field)'}),
          
          
            'Fourth_Skill_category'                      :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category (Optional field)'}),
            'Fourth_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill | Skill | Skill (Optional field)'}),
            
            
            'Fifth_Skill_category'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category (Optional field)'}),
            'Fifth_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill | Skill | Skill (Optional fieldl)'}),
            
            
            
            # 'Sixth_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill six (This field is optional)'}),
            # 'Seventh_Skill'                     :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill seven (This field is optional)'}),


            'First_Language'                     :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'First language'}),
            'Second_Language'                   :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Second language (This field is optional)'}),
            'Third_Language'                    :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Third language (This field is optional)'}),
            'Fourth_Language'                   :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fourth language (This field is optional)'}),
            
        }








class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact

        fields = [
            'Name',
            'Email',
            'Professional_Status',
            'Country',
            'How_you_came_to_know_about_us',
            'Message'
        ]

        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'Email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Email'}),
            'Professional_Status': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Are you a student?'}),
            'Country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Country'}),
            'How_you_came_to_know_about_us': forms.TextInput(attrs={'class':'form-control', 'placeholder':'How you came to know about us'}),
            'Message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Tell us your message/feedback/suggestions', 'maxlength': '1500',}),

        }