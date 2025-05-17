from NotificationInterface import notification_interface

class abstract_notification (notification_interface):
    name = "John Doe"
    
    def setReceiver(self, name):
        self.name = name
        return self.name