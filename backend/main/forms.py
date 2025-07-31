from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesFrom(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content', 'date']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Title', 'type': 'text'}),
            'content': Textarea(attrs={'placeholder': 'Content', 'type': 'text'}),
            'date': DateTimeInput(attrs={'placeholder': 'Date', 'type': 'date'})
        }