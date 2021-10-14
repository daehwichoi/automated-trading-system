# Abstract API

from abc import ABCMeta, abstractmethod
from typing import List

class AbstractAPI(metaclass=ABCMeta):
    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def connect(self, id: str, password: str, cert_password: str) -> None:
        pass

    @abstractmethod
    def get_accounts(self) -> List[str]:
        pass

    @abstractmethod
    def get_every_stock_codes(self) -> List[str]:
        pass