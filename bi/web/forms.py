from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import DateTimeField
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit,ButtonHolder, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, Field,TabHolder, Tab




class CreateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','password']
        labels = {'first_name':'Nombres',
        'last_name':'Apellidos',
        'email':'Correo',
        'password':'Contraseña'}

        widgets = {
          'password': forms.PasswordInput(),
          'email': forms.EmailInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
            Div(
                Div(
                    Field('first_name',css_class="form-control"),
                    Field('last_name',css_class="form-control"),
                    Field('email',css_class="form-control"),
                    Field('password',css_class="form-control"),
                    css_class=' col-lg-6'
                    ),
                css_class='formcontainer'
                ),
            css_class='row'
            ),
            )

        self.fields['first_name'].required=True
        self.fields['last_name'].required=True
        self.fields['email'].required=True
        self.fields['password'].required=True


class CreateUserRolForm(forms.ModelForm):

    class Meta:
        model = SystemUser
        fields = ['rol','identification','cellphone']
        labels = {'rol':'Rol del usuario',
        'identification': 'Número de identificación',
        'cellphone':'Número de celular'}

    def __init__(self, *args, **kwargs):
        super(CreateUserRolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
            Div(
                Div(
                    Field('identification',css_class="form-control"),
                    Field('cellphone',css_class="form-control"),
                    Field('rol',css_class="form-control"),
                    css_class='col-lg-6'
                    ),

                css_class='form_container'
                ),
            css_class='row'
            ),
            )
        self.fields['rol'].required=True




class CreateConnectionForm(forms.ModelForm):

    class Meta:
        model = ConectionData
        fields = ['dbname','username','password','host','port','dbtype']
        labels = {'dbname':'Nombre de la base de datos',
        'username': 'Nombre de usuario',
        'password': 'Contraseña',
        'host': 'Host',
        'port': 'Puerto',
        'dbtype':'Tipo de base de datos'}

    def __init__(self, *args, **kwargs):
        super(CreateConnectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
            Div(
                Div(
                    Field('dbname',css_class="form-control"),
                    Field('username',css_class="form-control"),
                    Field('password',css_class="form-control"),
                    Field('host',css_class="form-control"),
                    Field('port',css_class="form-control"),
                    Field('dbtype',css_class="form-control"),
                    css_class='col-lg-6'
                    ),

                css_class='form_container'
                ),
            css_class='row'
            ),
            )
        self.fields['dbname'].required=True
        self.fields['username'].required=True
        self.fields['password'].required=True
        self.fields['host'].required=True
        self.fields['port'].required=True
        self.fields['dbtype'].required=True






