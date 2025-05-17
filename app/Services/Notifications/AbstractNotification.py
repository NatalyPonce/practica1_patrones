from NotificationInterface import NotificationInterface

class abstract_notification (NotificationInterface):
    name = "John Doe"
    
    def setReceiver(self, name):
        self.name = name
        return self.name