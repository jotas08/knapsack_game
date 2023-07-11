from abc import abstractmethod


class Subject:

    @abstractmethod
    def add_event(self, observer):
        pass

    @abstractmethod
    def del_event(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

