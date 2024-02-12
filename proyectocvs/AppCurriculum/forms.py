from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ExperienciaFormulario(forms.Form):
    cargo = forms.CharField(label='Cargo', max_length=100)
    empresa = forms.CharField(label='Empresa', max_length=100)
    periodo_inicio = forms.DateField(label='Fecha Inicio')
    periodo_fin = forms.DateField(label='Fecha Fin')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'cargo',
            'empresa',
            'fecha_inicio',
            'fecha_fin',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class EstudioFormulario(forms.Form):
    institucion = forms.CharField(label='Institucion', max_length=100)
    titulo = forms.CharField(label='Titulo', max_length=100)
    periodo_inicio = forms.DateField(label='Fecha Inicio')
    periodo_fin = forms.DateField(label='Fecha Fin')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'institucion',
            'titulo',
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
