from django import forms


class RegUser(forms.Form):
    email = forms.CharField(label='Логин(e-mail):', max_length=25)
    password = forms.CharField(label='Пароль:', max_length=25, widget=forms.PasswordInput())
    password_check = forms.CharField(label='Еще раз:', max_length=25, widget=forms.PasswordInput())


class LoginUser(forms.Form):
    email = forms.CharField(label='Логин(e-mail):', max_length=25)
    password = forms.CharField(label='Пароль:', max_length=25, widget=forms.PasswordInput())


class AddToCart(forms.Form):
    quantity = forms.IntegerField(initial=1, label='Количество:',
                                  widget=forms.NumberInput(attrs={'class': 'add_to_cart'}))


class ModifyCartForm(forms.Form):
    product = forms.CharField(label='Товар:', disabled=True)
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(label='Количество')
