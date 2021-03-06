from django import forms

form_css_class = 'form-control form-control-user'
profile_form = 'form-control'


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(
        attrs={'class': form_css_class, 'name': "email", 'required': "", 'placeholder': "Email"}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'class': form_css_class, 'name': "password", 'required': "", 'placeholder': "Password"}))


class RegisterForm(forms.Form):
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': form_css_class, 'name': "last_name", 'required': "", 'placeholder': "Last Name"}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': form_css_class, 'name': "first_name", 'required': "", 'placeholder': "First Name"}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': form_css_class, 'name': "username", 'required': "", 'placeholder': "Username"}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(
        attrs={'class': form_css_class, 'name': "email", 'required': "", 'placeholder': "Email Address"}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'class': form_css_class, 'name': "password", 'required': "", 'placeholder': "Password"}))
    password_confirm = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'class': form_css_class, 'name': "password_confirm", 'required': "", 'placeholder': "Repeat Password"}))


class UserProfileForm(forms.Form):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'style': "border-color: rgb(28, 40, 38)", 'onchange': 'readURL(this)'}), required=False)
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': profile_form, 'name': "username"}), required=False)
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': profile_form, 'name': "first_name"}), required=False)
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': profile_form, 'name': "last_name"}), required=False)
    website = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': profile_form, 'name': "website"}), required=False)
    address = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': profile_form, 'name': "address"}), required=False)
    city = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': profile_form, 'name': "city"}), required=False)
    country = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': profile_form, 'name': "country"}), required=False)
