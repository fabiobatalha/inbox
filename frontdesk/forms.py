from django import forms


class DepositForm(forms.Form):
    md5_sum = forms.CharField(max_length=32)
    package = forms.FileField()
    depositor = forms.CharField(max_length=16)
