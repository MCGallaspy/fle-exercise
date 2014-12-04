from django import forms

COMPARISON_CHOICES = [('gt', 'greater than'), ('lt', 'less than')]

class MovieFilterForm(forms.Form):
  critic_score_op = forms.ChoiceField(choices=COMPARISON_CHOICES, required=False)
  critic_score_threshold = forms.IntegerField(min_value=0, max_value=100, required=False)
  audience_score_op = forms.ChoiceField(choices=COMPARISON_CHOICES, required=False)
  audience_score_threshold = forms.IntegerField(min_value=0, max_value=100, required=False)
  runtime_op = forms.ChoiceField(choices=COMPARISON_CHOICES, required=False)
  runtime_threshold = forms.IntegerField(min_value=0, required=False)
