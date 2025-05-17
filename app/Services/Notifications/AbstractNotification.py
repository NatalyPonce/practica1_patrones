from NotificationInterface import NotificationInterface

class abstract_notification (NotificationInterface):
    contact = ""
    def setReceiver(self, contact):
        self.contact = contact
        return self
    