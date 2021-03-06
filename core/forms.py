from __future__ import unicode_literals
from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):

	name = forms.CharField(label='Nomes')
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea())

	def send_mail(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		message = self.cleaned_data['message']
		message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name, email, message)
		send_mail(
			'Contato Eletronic & Cia', message, settings.DEFAULT_FROM_EMAIL,
			[settings.DEFAULT_FROM_EMAIL]
		)

