from django import forms
from .models import choice

class QuizForm(forms.Form):
     def _init_(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super(QuizForm, self)._init_(*args, **kwargs)

        if questions:
            for question in questions:
                choices = [(choice.id, choice.choice_text) for choice in question.choice_set.all()]
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.question_text,
                    choices=choices,
                    widget=forms.RadioSelect
                )