from django import forms

class EmailForm(forms.Form):
    email_address = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    receivers = forms.CharField()
    subject = forms.CharField()
    text = forms.CharField(widget = forms.Textarea)


    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['email_address'].widget.attrs.update({'class':'form-control', 'placeholder':'Your Email Address...'})
        self.fields['password'].widget.attrs.update({'class':'form-control', 'placeholder':'Your Password...'})
        self.fields['receivers'].widget.attrs.update({'class':'form-control', 'placeholder':'List of receipients(Comma separated)'})
        self.fields['subject'].widget.attrs.update({'class':'form-control', 'placeholder':'Subject'})
        self.fields['text'].widget.attrs.update({'class':'form-control', 'placeholder': 'Enter Message'})