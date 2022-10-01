from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django import forms
from .models import *

#FORMS DE VETERINARIO
class VeterinarioForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='Usuario',widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Nombre de usuario"
        }
    ))
    password = forms.CharField(max_length=120, label='contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    rol=forms.ModelChoiceField(label='Rol', queryset=Group.objects.all(), widget=forms.Select(
        attrs={
            'class':'form-select'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))
    nombres= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    apellidos= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    tipo_documento= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    num_documento= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    celular= forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    num_profesional= forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    class Meta:
        model= Veterinario
        fields= ['num_profesional']

#FORMS DE CLIENTE
class ClienteForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='Usuario',widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Nombre de usuario"
        }
    ))
    password = forms.CharField(max_length=120, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    rol=forms.ModelChoiceField(label='Rol', queryset=Group.objects.all(), widget=forms.Select(
        attrs={
            'class':'form-select'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))
    nombres= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    apellidos= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    tipo_documento= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    num_documento= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    celular= forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    class Meta:
        model= cliente
        fields= []

#FORMS DE GRUPOS
class GroupsForm(forms.ModelForm):
    name = forms.CharField(max_length=80, label='Rol', widget=forms.TextInput(
        attrs={'class': 'form-control'
        }
    ))
    permisos=forms.ModelMultipleChoiceField(label='Permisos',
        queryset=Permission.objects.filter(content_type__app_label='veterinariaapp'), 
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select'
            }
        )
    )
    class Meta:
        model= Group
        fields= '__all__'

#FORMS PARA EL LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Usuario'
        }
    ))
    
    password = forms.CharField(max_length=80, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

#FORMS DE REGISTRO
class RegistroForm(forms.ModelForm):
    
    mascota=forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select(
        attrs={
            'class':'form-select'
        }
    ))
    veterinario = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    num_historial= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    fecha= forms.CharField(max_length=120, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    motivo= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    anamnesicos= forms.CharField(max_length=20, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    diagnostico= forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    tratamiento= forms.CharField(max_length=10, widget=(forms.TextInput(
        attrs={
            'class': "form-control"
        }
    )))
    class Meta:
        model= Registro
        fields= ['num_historial']
    