from abc import ABC, abstractmethod
from typing import Tuple


class GetUrlInterface(ABC):
    """Request Url Interface"""

    @abstractmethod
    def fetch(self, url: str) -> Tuple[int, str]:
        """Must Implement"""
        raise Exception("Must implement fetch")
