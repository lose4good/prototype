'''
Created on Nov 24, 2013

@author: ArulSamuel
'''
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm #Django automatically create a form out of the fields
from accounts.models import WeightLoser

class LoginForm(forms.Form):
        username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','size':'20'}))
        password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','size':'20'},render_value=False))
        

class RegistrationForm(ModelForm): #Extend ModelForm
        fname        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
        lname           = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','size':'22'}))
        emailId           = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','size':'50'}))
        password        = forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Password','size':'50'}))
        #Build in widget (django) - password **** type
        passworda       = forms.CharField(label=(u'Re-Type Password'), widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Re-Type Password','size':'50'}))
        CHOICES = (('0', 'Male',), ('1', 'Female'),)
        gender          = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
        dob        = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Date Of Birth','size':'22'}))
        currentWeight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Current Weight','size':'22'}))

        class Meta:
                model = WeightLoser #power of ModelForm here.
                exclude = ('user',)   #Exclude the creation of these field (above4)

        #def clean_emailId(self):
                #data that comes after posting to view
        #        try:
        #                User.objects.get(emailId=emailId)
        #        except User.DoesNotExist:
        #                return emailId
        #        raise forms.ValidationError("This email Id is already registered with the system.")

        #def clean_password(self):
        #        password = self.cleaned_data['password']  #data that comes after posting to view
        #       password1 = self.cleaned_data['password1']
        #        if password != password1:
        #            raise forms.ValidationError("The passwords did not match. Please try again.")
        #        return password

        #Clean method handles all fields whereas password fails validation for password1
        def clean(self):
                print 'What is it '+self.cleaned_data['passworda']
                emailId = self.cleaned_data['emailId']
                try:
                        User.objects.get(email=emailId)
                        raise forms.ValidationError("This email Id is already registered with the system.")
                except User.DoesNotExist:
                        pass #return emailId
                
            
            
                if self.cleaned_data['password'] != self.cleaned_data['passworda']:
                        print ' reached here'
                        raise forms.ValidationError("The passwords did not match.  Please try again.")
                
                return self.cleaned_data
        
        