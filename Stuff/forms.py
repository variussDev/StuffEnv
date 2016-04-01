from django.utils.translation import ugettext_lazy as _
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from .models import Part
from .models import PartPicture


class NewPart(forms.ModelForm):
    
    class Meta:
        model = Part
        fields = [ 
            'partName',
            'partCount',
            'partDescription',
            'partType',
        ]

    def __init__( self, *args, **kwargs):
        super(NewPart, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_action =""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
                layout.Fieldset(
                    _(u"Dane podstawowe"),
                    layout.Field("partName", css_class="input-block-level"),
                    layout.Field("partCount", css_class="input-block-level"),
                    layout.Field("partType", css_class="input-block-level"),
                    layout.Field("partDescription",  css_class="input-block-level", rows="4" ),
                ),
                bootstrap.FormActions(
                    layout.Submit("submit", _(u"Zapisz")),
                ),
        )

        
class NewPartPicture( forms.ModelForm ):
    class Meta:
        model = PartPicture
        fields = [
            'picture',
            'picLabel',
        ]
    def __init__( self, *args, **kwargs):
        super( NewPartPicture, self ).__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
            layout.Field("picLabel", css_class="input-block-level"),
            layout.Field("picture", css_class="input-block-level"),
            bootstrap.FormActions(
                layout.Submit("submit", _(u"Zapisz") ),
            ),
        )

        
class Part_to_picture_test( forms.Form ):
    partField = forms.ModelChoiceField( queryset = Part.objects.all()  )
    partImage = forms.ImageField( _(u"Zdjęcie") )

    def __init__( self, *args, **kwargs):
        super( Part_to_picture_test, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action =""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
                layout.Field("partField", css_class="input-block_level"),
                layout.Field("partImage", css_class="btn btn-primary"),
                bootstrap.FormActions(
                    layout.Submit("submit", _(u"Zapisz")),
                ),
        )


