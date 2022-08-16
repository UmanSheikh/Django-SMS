from django.shortcuts import render, HttpResponse
from twilio.rest import Client
# Create your views here.
def index(request):
    return render(request, 'home.html')

def send(request):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    if request.method == 'POST':
        account_sid = 'Your SID'
        auth_token = 'Your Token'
        client = Client(account_sid, auth_token)
        msg = request.POST.get('msg')
        message = client.messages \
                        .create(
                            body=msg,
                            from_='Your Twiliow Number',
                            to='Number of client'
                        )

        print(message.sid)
        return HttpResponse("<h1>Your Message has been sent</h1>")
    else:
        return HttpResponse("False")