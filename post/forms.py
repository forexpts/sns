from django import forms

class PostForm(forms.Form):
    content = forms.CharField(max_length=5000, 
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False, label='画像')
    VISIBILITY_CHOICES = [
        ('public', '公開'),
        ('private', '非公開'),
    ]
    visibility = forms.ChoiceField(choices=VISIBILITY_CHOICES,
                                   required=True)
    