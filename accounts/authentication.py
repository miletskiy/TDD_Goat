
import requests
import sys
from accounts.models import ListUser


class PersonaAuthenticationBackend(object):
    """docstring for PersonAuthenticationBackend"""

    def authenticate(self, assertion):
        # Send the assertion to Mozilla's verifer servise.
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('sending to Mozilla', data, file=sys.stderr)
        # print('sending to Mozilla', data, {file:sys.stderr})
        # print('login view', {file:sys.stderr})

        resp = requests.post('https://verifier.login.persona.org/verify', data = data)
        # resp = requests.post('https://verifer.login.persona.org/verify', data )

        print('got', resp.content, file=sys.stderr)
        # print('got', resp.content, {file:sys.stderr})

        # Did the verifer respond?
        if resp.ok:
            # Parse the response
            verification_data = resp.json()

            # Check if the assertion was valid
            if verification_data['status'] == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.objects.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)




