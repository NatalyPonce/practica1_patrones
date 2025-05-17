from EmailNotification import EmailNotification
from SmsNotification import SmsNotification
from WhatsappNotification import WhatsappNotification

def main():
    
    nombre = 'Jhon Doe'
    emailNot = EmailNotification('200237@esen.edu.sv', nombre)
    emailNot.notificar()

    Sms = SmsNotification('502', '263791733', nombre)
    Sms.notificar()

    whats = WhatsappNotification('502', '263791733', nombre)
    whats.notificar()


main()