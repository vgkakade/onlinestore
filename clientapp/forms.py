from django import forms
from . import models
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # self.fields['email'].label ='First name'       one more way to add label to field
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Email'

    # def clean(self):
    #     form_cleaned_data = super().clean()         # cleans all of the form data
    #     pass1 = form_cleaned_data['password1']
    #     pass2 = form_cleaned_data['password2']
    #     if pass1 != pass2:
    #         raise forms.ValidationError("Password Mismatch")


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = models.UserAddress
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['pincode'].widget.attrs['placeholder']='Enter pincode'
        self.fields['city'].widget.attrs['readonly']=True
        self.fields['state'].widget.attrs['readonly'] = True