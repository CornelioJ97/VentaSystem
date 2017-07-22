from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MyAuthForm
from django.contrib.auth import authenticate, login, logout

def home(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/facturacion/')
	form = MyAuthForm()
	return render(request, 'login.html', {'form': form})

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')

def log_in(request):
	if request.method == 'POST':
		form = MyAuthForm(data=request.POST)

		if form.is_valid():
			user = authenticate(username=request.POST['username'], password=request.POST['password'])

			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/facturacion/')
				else:
					return render(request, 'login.html', {'form': form} )
			else:
				return render(request, 'login.html', {'form': form} )
		else:
			return render(request, 'login.html', {'form': form} )

	else:
		return HttpResponseRedirect('/')