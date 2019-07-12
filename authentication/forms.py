from django import forms

class UserRegistrationForm(forms.Form):

    first_name = forms.CharField(
        required = True,
        label = 'First Name',
        max_length = 32,
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )

    last_name = forms.CharField(
        required = True,
        label = 'Last Name',
        max_length = 32,
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )


    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32,
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )
    email = forms.EmailField(
        required = True,
        label = 'Email',
        max_length = 32,
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )
    
    contact = forms.CharField(
        required = True,
        label = 'Phone No.',
        max_length = 32,
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput(
            attrs={
            "class": "form-control",
            }
        )
    )

    confirm_password = forms.CharField(
        required = True,
        label = 'Confirm Password',
        max_length = 32,
        widget = forms.PasswordInput(
            attrs={
            "class": "form-control",
            }
        )
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        pass2 = self.cleaned_data.get("confirm_password")
        if password != pass2:
            raise forms.ValidationError("Passwords don't match!")

        return password



class UserLoginForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32,
        widget = forms.TextInput(
            attrs={
            "class": "form-control",
            }
        )
    )

    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput(
            attrs={
            "class": "form-control",
            }
        )
    )