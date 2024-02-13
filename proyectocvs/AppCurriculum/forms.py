from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ExperienciaFormulario(forms.Form):
    cargo = forms.CharField(label='Cargo', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    empresa = forms.CharField(label='Empresa', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.CharField(label='Pais', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    periodo_inicio = forms.IntegerField(label='Fecha Inicio',widget=forms.TextInput(attrs={'class': 'form-control'}))
    periodo_fin = forms.IntegerField(label='Fecha Fin',widget=forms.TextInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'cargo',
            'empresa',
            'description',
            'pais',
            'fecha_inicio',
            'fecha_fin',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class EstudioFormulario(forms.Form):
    institucion = forms.CharField(label='Institucion', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    titulo = forms.CharField(label='Titulo', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.CharField(label='Pais', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    periodo_inicio = forms.IntegerField(label='Fecha Inicio',widget=forms.TextInput(attrs={'class': 'form-control'}))
    periodo_fin = forms.IntegerField(label='Fecha Fin',widget=forms.TextInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'institucion',
            'titulo',
            'description',
            'pais',
            'fecha_inicio',
            'fecha_fin',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class IdiomaFormulario(forms.Form):
    idioma = forms.CharField(label='Idioma', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    nivel = forms.CharField(label='Nivel', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'idioma',
            'nivel',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class DataUsuarioFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(label='Apellido', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(label='Biografía', max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label='Teléfono', max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_facebook = forms.CharField(label='URL facebook', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_twitter = forms.CharField(label='URL twitter', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_github = forms.CharField(label='URL github', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_youtube = forms.CharField(label='URL youtube', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_linkedin = forms.CharField(label='URL linkedin', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'nombre',
            'apellido',
            'biografía',
            'telefono',
            'url_facebook',
            'url_twitter',
            'url_github',
            'url_youtube',
            'url_linkedin',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class SkillFormulario(forms.Form):
    aptitud = forms.CharField(label='Aptitud', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'aptitud',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )