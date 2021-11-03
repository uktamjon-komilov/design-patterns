from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass