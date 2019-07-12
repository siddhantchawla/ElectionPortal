from django import forms

post = (
        ('-','---SELECT---'),
        ('PR','President'),
        ('VP','Vice President'),
        ('SS','Sports secretary'),
        ('ES','Enviornment secretary'),
        ('CS','Cultural secretary'),
    )

class SessionStartForm(forms.Form):
    post = forms.CharField(
        required = True,
        label = 'Branch',
        max_length = 64,
        widget = forms.Select(
            choices = post,
            attrs={
            "class": "form-control",
            }
            )

    )
    year = forms.IntegerField(
        required = True,
        label = 'year',
    )