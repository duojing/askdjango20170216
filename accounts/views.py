from django.shortcuts import redirect, render
from accounts.forms import SignupForm
from django.conf import settings

def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)

    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
        })

def profile(request):
    return render(request, 'accounts/profile.html')