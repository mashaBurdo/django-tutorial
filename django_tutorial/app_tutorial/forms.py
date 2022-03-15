from django import forms


class BookForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    # TODO: page_number and description