from AbstractNotification import abstract_notification

class WhatsappNotification(abstract_notification):
    def __init__(self, codigo, numero, name):
        self.codigo = codigo
        self.numero = numero
        super().setReceiver(name)
        
    def notificar(self):
        print(f"Sent to {self.name} WhatsApp message to +{self.codigo} {self.numero}")