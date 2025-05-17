from AbstractNotification import AbstractNotification
class EmailNotification(AbstractNotification):
    def __init__(self, recipient_email, subject, message):


    def send(self):
        # Logic to send email notification
        print(f"Sending email to {self.recipient_email} with subject '{self.subject}' and message '{self.message}'")