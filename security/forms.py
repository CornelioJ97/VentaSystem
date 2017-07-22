from django.contrib.auth.forms import AuthenticationForm

class MyAuthForm(AuthenticationForm):
	def __init__(self, *args, **kargs):
		super(MyAuthForm, self).__init__(*args, **kargs)

		self.base_fields['username'].widget.attrs['class'] = 'form-control'
		self.base_fields['password'].widget.attrs['class'] = 'form-control'
