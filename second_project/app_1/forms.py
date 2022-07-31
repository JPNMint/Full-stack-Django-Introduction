from django import forms
from django.core import validators
from app_1.models import Webpage

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifyemail = forms.EmailField(label = 'Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        if all_clean_data['email'] != all_clean_data['verifyemail']:
            raise forms.ValidationError("Email doesn't match!")


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise froms.ValidationError("Bot found!")
    #     return botcatcher



class NewWebpage(forms.ModelForm):
    class Meta:
        model = Webpage
        fields ='__all__'
