from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label='E-Mail')
    order = forms.CharField(max_length=100000, widget=forms.Textarea)

