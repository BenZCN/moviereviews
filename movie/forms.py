from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super(ModelForm, self)._init_(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Review
        fields = ['text', 'watchAgain']
        labels = {'watchAgain': ('Watch Again')
        }
        widgets = {'text': Textarea(attrs={'rows': 4}),
        }