from django import forms

post = (
        ('-','---SELECT---'),
        ('President','President'),
        ('Vice President','Vice President'),
        ('Sports secretary','Sports secretary'),
        ('Environment secretary','Environment secretary'),
        ('Cultural secretary','Cultural secretary'),
    )

class SessionStartForm(forms.Form):
    post = forms.CharField(
        required = True,
        label = ' Post ',
        max_length = 64,
        widget = forms.Select(
            choices = post,
            attrs={
            "class": "form-control",
            }
            )

    )
    # year = forms.IntegerField(
    #     required = True,
    #     label = 'year',
    # )