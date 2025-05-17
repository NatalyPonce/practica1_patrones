from AbstractNotification import abstract_notification

class SmsNotification(abstract_notification):
    def __init__(self, codigo, numero, name):
        self.codigo = codigo
        self.numero = numero
        super().setReceiver(name)
        
    def notificar(self):
        print(f"Sent to {self.name} SMS to +{self.codigo} {self.numero}")