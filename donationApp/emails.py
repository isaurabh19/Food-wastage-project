from django.core.mail import EmailMessage

def send_email(subject,body,to):
    e = EmailMessage()
    e.subject = subject
    e.body = body
    e.to = to
    e.send()
