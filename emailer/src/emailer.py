import smtplib
from email.message import EmailMessage

class EmailerCreds(object):

    def __init__(self, creds_file):
        f = open(creds_file, 'r')
        self.server = 'smtp.gmail.com'
        self.user_name = f.readline()
        self.password = f.readline()

class Emailer(object):

    def __init__(self, creds):
        self.server = smtplib.SMTP_SSL(creds.server, 465)
        self.server.login(creds.user_name.strip(), creds.password.strip())

    def send_text(self, email_address, email_text):
        self.server.sendmail(email_address, email_address, email_text)

    def send_file(self, recipient, sender, path, subject=None):
        msg = EmailMessage()
        if subject is not None:
            msg["Subject"] = subject
        else:
            msg["Subject"] = "Sent from Emailer"
        msg["To"] = recipient
        msg["From"] = sender
        with open(path, 'rb') as fp:
            msg.add_attachment(
                fp.read(),
                maintype="application",
                subtype="octet-stream",
                filename=path
            )

        self.server.send_message(msg)
