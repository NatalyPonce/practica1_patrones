from AbstractNotification import abstract_notification

class EmailNotification(abstract_notification):
    def __init__(self, email, name):
        self.email = email
        super().setReceiver(name)
        
    def notificar(self):
        print(f"Sent to {self.name} email to {self.email}")