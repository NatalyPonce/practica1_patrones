from NotificationInterface import notification_interface

class abstract_notification (notification_interface):    
    def setReceiver(self, name):
        self.name = name
        return self.name