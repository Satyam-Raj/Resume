from django import forms
from .models import Professional, Contact


class Profile_update_form(forms.ModelForm):
    class Meta:
        model = Professional
        fields = [
            'image',
            'First_Name',
            'Last_Name',
            'Age',

            'Mobile_Number',
            'Email',
            'Address',
           
            'Introduction',
            'Currently_or_was_working_for',
            'Description',

            'First_Experience',
            'First_Experience_Description',

            'Second_Experience',
            'Second_Experience_Description',

            'Third_Experience',
            'Third_Experience_Description',

            'Fourth_Experience',
            'Fourth_Experience_Description',

            'Fifth_Experience',
            'Fifth_Experience_Description',

            'School',
            'School_Description',

            'College',
            'College_Description',

           'First_Skill',
           'Second_Skill',
           'Third_Skill',
           'Fourth_Skill',
           'Fifth_Skill',
        #    'Sixth_Skill',
        #    'Seventh_Skill',

           'Fist_Language',
           'Second_Language',
           'Third_Language',
        ]



        widgets = {

            

            'First_Name'                         :          forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your First Name','onfocus': 'this.placeholder = ''','onblur': "this.placeholder = 'About Your organization'",}),
            'Last_Name'                          :          forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Last Name'}),
            'Age'                                :          forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Age'}),

            'Mobile_Number'                     :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your mobile number'}),
            'Email'                             :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your email'}),
            'Address'                           :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your address'}),

            'Introduction'                      :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Introduce yourself','maxlength': '900'}),
            'Currently_or_was_working_for'      :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'For which company you are/were working for (This field is optional)'}),
            'Description'                       :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'It is ok to brag about your desingnation, promotions and achievements (This field is optional)', 'maxlength': '900',}),


            'First_Experience'                  :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title | Company Name | Duration | Location (This field is optional)'}),
            'First_Experience_Description'      :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),
            
            'Second_Experience'                 :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title | Company Name | Duration | Location (This field is optional)'}),
            'Second_Experience_Description'     :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),

            'Third_Experience'                  :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title | Company Name | Duration | Location (This field is optional)'}),
            'Third_Experience_Description'      :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),

            'Fourth_Experience'                 :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title | Company Name | Duration | Location (This field is optional)'}),
            'Fourth_Experience_Description'     :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),

            'Fifth_Experience'                  :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Title | Company Name | Duration | Location (This field is optional)'}),
            'Fifth_Experience_Description'      :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description (This field is optional)','maxlength': '900'}),


            'School'                            :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title | Institution Name | Duration | Location'}),
            'School_Description'                :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description','maxlength': '900'}),

            'College'                           :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title | Institution Name | Duration | Location'}),
            'College_Description'               :           forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the description','maxlength': '900'}),


            'First_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill One'}),
            'Second_Skill'                      :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill two'}),
            'Third_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill three'}),
            'Fourth_Skill'                      :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill four (This field is optional)'}),
            'Fifth_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill five (This field is optional)'}),
            # 'Sixth_Skill'                       :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill six (This field is optional)'}),
            # 'Seventh_Skill'                     :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill seven (This field is optional)'}),


            'Fist_Language'                     :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'First language'}),
            'Second_Language'                   :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Second language (This field is optional)'}),
            'Third_Language'                    :           forms.TextInput(attrs={'class':'form-control', 'placeholder':'Third language (This field is optional)'}),
            
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