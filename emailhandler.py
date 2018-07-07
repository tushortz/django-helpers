import smtplib
import os


def send_email(recipients, subject, body):
    gmail_user = os.environ.get("EMAIL") or "myemail@gmail.com"
    password = os.environ.get("PASSWORD") or "mypassword"

    gmail_pwd = password
    FROM = gmail_user
    TO = recipients if type(recipients) is list else [recipients]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print('successfully sent the mail')
