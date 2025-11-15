from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "anons", "FULL", "date"]

        widgets = {
            "title": TextInput(attrs={
                "placeholder": "Название",
                "class": "form-control"
            }),
            "anons": TextInput(attrs={
                "placeholder": "Анонс",
                "class": "form-control"
            }),
            "FULL": Textarea(attrs={
                "placeholder": "Статья",
                "class": "form-control"
            }),
            "date": DateInput(attrs={
                "placeholder": "Дата",
                "class": "form-control",
                "type": "date"
            })
        }