from django import forms
from .models import post, category, comment

# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]
choices = category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class postform(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter your post title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control',}),
            'author' : forms.TextInput(attrs={'class' : 'form-control', 'value':'', 'id':'newman', 'type':'hidden'}),
            # 'author' : forms.Select(attrs={'class' : 'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class' : 'form-control'}),
        }
        
        
class Editform(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'title_tag', 'body', 'snippet')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter your post title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control',}),
            # 'author' : forms.Select(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class' : 'form-control'}),
        }
        
        
class Commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('name', 'body',)
        
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control',}),
            # 'title_tag' : forms.TextInput(attrs={'class' : 'form-control',}),
            # 'author' : forms.Select(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            # 'snippet' : forms.Textarea(attrs={'class' : 'form-control'}),
            
        }