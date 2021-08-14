from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()



class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model = CustomUser
        fields = ('username', 'email')



class CustomUserChangeForm(UserChangeForm):

    class Meta:

        model = CustomUser
        fields = ('username', 'email')





class LoginForm(forms.Form):

    email = forms.EmailField(label='E-Mail')
    password = forms.CharField(max_length=15, label='Şifre', widget=forms.PasswordInput)

    def clean(self):

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:

            user = authenticate(email=email, password=password)

            if not user:

                raise forms.ValidationError('Kullanıcı adı ya da parola yanlış')

        return super(LoginForm, self).clean()



class RegisterForm(forms.ModelForm):

    AUTHOR_CHOICES = (
        ('Manager', 'Yönetici'),
    )

    email = forms.EmailField(label='E-Mail')
    username = forms.ChoiceField(choices = AUTHOR_CHOICES, label='Yönetici Yetkisi')
    first_name = forms.CharField(max_length=15, label='İsim')
    last_name = forms.CharField(max_length=15, label='Soyisim')
    password1 = forms.CharField(max_length=15, label='Şifre', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=15, label='Şifre Tekrar', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]



    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:

            raise forms.ValidationError('Parolalar eşleşmiyor tekrar deneyin')

        return password2





class PersonnelCreateForm(forms.ModelForm):

    PERSONNEL_CHOICES = (
        ('Electric', 'Elektrik Çalışanı'),
        ('Elevator', 'Asansör Çalışanı'),
        ('Garden', 'Bahçe Çalışanı'),
        ('Apartment', 'Bina Çalışanı'),
    )

    email = forms.EmailField(label='E-Mail')
    username = forms.ChoiceField(choices=PERSONNEL_CHOICES, label='İş Bölümü')
    first_name = forms.CharField(max_length=15, label='İsim')
    last_name = forms.CharField(max_length=15, label='Soyisim')
    password1 = forms.CharField(max_length=15, label='Şifre', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=15, label='Şifre Tekrar', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:

            raise forms.ValidationError('Parolalar eşleşmiyor tekrar deneyin')

        return password2





class ResidentCreateForm(forms.ModelForm):

    RESIDENT_CHOICES = (
        ('Host', 'Ev Sahibi'),
        ('Tenant', 'Kiracı'),
    )

    email = forms.EmailField(label='E-Mail')
    username = forms.ChoiceField(choices=RESIDENT_CHOICES, label='Durum')
    first_name = forms.CharField(max_length=15, label='İsim')
    last_name = forms.CharField(max_length=15, label='Soyisim')
    password1 = forms.CharField(max_length=15, label='Şifre', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=15, label='Şifre Tekrar', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]



    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:

            raise forms.ValidationError('Parolalar eşleşmiyor tekrar deneyin')

        return password2





class ProblemForm(forms.ModelForm):

    class Meta:

        model = Problems

        fields = [
            'problem',
            'content',
        ]