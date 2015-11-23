

import sys
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.shortcuts import redirect

# Create your views here.

def login(request):
    # print('login view', {file:sys.stderr})
    print('login view', file = sys.stderr)
    # print('login view', file=sys.stdout)
    # user = PersonaAuthenticationBackend().authenticate(request.POST['assertion'])
    # user = authenticate(assertion = request.POST['assertion'])
    user = authenticate(assertion = request.POST.get('assertion'))
    if user is not None:
        auth_login(request, user)
    return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('/')



