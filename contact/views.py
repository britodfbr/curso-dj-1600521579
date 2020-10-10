from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    send = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # enviar email
        name = request.POST.get('name', '')
        em = request.POST.get('email', '')
        content = request.POST.get('message', '')
        email = EmailMessage(
            "Mensagem do Blog em Django",
            f"De: {name} <{em}> Escreveu: \n\n {content}",
            "no-responder@inbox.mailtrap.io",
            ["contato@incolume.com.br"],
            reply_to=[em]
        )
        try:
            email.send()
            send = True
        except:
            send = False
    context = {
        'form': ContactForm,
        'success': send
    }
    return render(request, 'contact/contact.html', context)
