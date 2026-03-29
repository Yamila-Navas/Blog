from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    '''
    Formulario para enviar un correo electrónico sobre una entrada del blog.
    '''
    name = forms.CharField(max_length=25, label='Nombre')
    email = forms.EmailField(label='Tu correo electrónico')
    to = forms.EmailField(label='Correo electrónico del destinatario')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Comentarios')


class CommentForm(forms.ModelForm):
    '''
    Formulario para añadir un comentario a una entrada del blog.
    Basado en el modelo Comment.
    '''
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            'name': 'Nombre',
            'email': 'Correo electrónico',
            'body': 'Comentario',
        }


class SearchForm(forms.Form):
    '''
    Formulario para buscar entradas del blog.
    '''
    query = forms.CharField(label='Buscar')
