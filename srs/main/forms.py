from django import forms
from .models import CardSet, CardContent, CardCategory

class CreateNewCardSet(forms.Form):
    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description')

class CreateNewCard(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=CardSet.objects.get(name='Korean 625 Words').cardcategory_set.all(), 
                                      empty_label="None", required=False)
    word_en = forms.CharField(label='Word (EN)')
    word_ko = forms.CharField(label='Word (KO)')
    association = forms.CharField(label='Text', required=False)
    image = forms.ImageField(label='Image', required=False)
    audio = forms.FileField(label='Audio', required=False)

    class Meta:
        model = CardContent
        fields = ['category', 'word_en', 'word_ko', 'association', 'image', 'audio']