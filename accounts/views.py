
# from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.


def persona_login(request):
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        login(request, user)
    return HttpResponse('OK')


#### Spiked version of our login view:
# def persona_login(request):
#     print('login view', file=sys.stderr)
#     # user = PersonaAuthenticationBackend().authenticate(request.POST['assertion'])
#     user = authenticate(assertion = request.POST['assertion'])
#     # user = authenticate(assertion = request.POST.get('assertion'))
#     if user is not None:
#         login(request, user)
#     return redirect('/')
