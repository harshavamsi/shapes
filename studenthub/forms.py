from django import forms
class PostForm(forms.Form):
    """Image upload form."""
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField(label='Tags',required=False)
    url = forms.CharField(label='URL',required=False)
    image = forms.ImageField(required=False)