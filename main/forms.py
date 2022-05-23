from logging import PlaceHolder
from django import forms

class Search(forms.Form):
    source=forms.CharField(label="Source", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Arad'}))
    destination=forms.CharField(label="Destination", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Bucharest'}))
    
class StoreC(forms.Form):
    
    graph=forms.CharField(widget=forms.Textarea(attrs={'name':'graph', 'rows':'7', 'cols':'50', 'placeholder':"City1 City2 value\nCity2 City3 valye"}))
    
    straight_line=forms.CharField(widget=forms.Textarea(attrs={'name':'staight_line', 'rows':'7', 'cols':'50', 'placeholder':"City1 heuristicsValye\nCity2 heuristicsValue"}))