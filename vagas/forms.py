from django  import forms
from .models import Lista

class VagasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        #self.status = kwargs.pop('status')
        super(VagasForm, self).__init__(*args, **kwargs)

        self.fields['candidato'].widget.attrs['disabled']    = True
        self.fields['unidade'].widget.attrs['disabled']      = True
        self.fields['modalidade'].widget.attrs['disabled']   = True
        self.fields['status'].widget.attrs['disabled']       = True
        self.fields['unidadeAtend'].widget.attrs['disabled'] = True
        self.fields['observacao'].widget.attrs['disabled']   = True

    class Meta:
        model = Lista
        fields = '__all__'