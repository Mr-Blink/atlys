class NotifierInterface:
    def notify(self, message: str):
        raise NotImplementedError

class ConsoleNotifier(NotifierInterface):
    def notify(self, message: str):
        print(f"Notification: {message}")

class NotificationFactory:
    @staticmethod
    def get_notifier(notifier_type: str) -> NotifierInterface:
        if notifier_type == "console":
            return ConsoleNotifier()
        raise ValueError(f"Notifier type '{notifier_type}' not supported.")