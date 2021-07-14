from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    #creating message subject and senders
    subject = "Welcome to MoringaTribune"
    sender = 'machariad196@gmail.com'

    #passing in the context variable

    text_content = render_to_string('email/newsemail.txt',{"name":name})
    html_content = render_to_string('email/newsemail.html',{"name":name})

    msg = EmailMultiAlternatives(subject, sender, text_content,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send
