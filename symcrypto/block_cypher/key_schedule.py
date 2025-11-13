from abc import ABC, abstractmethod
from typing import List


class KeyScheduleInterface(ABC):
    """
    интерфейс, предоставляющий описание функционала для процедуры расширения ключа
    (генерации раундовых ключей) (параметр метода: входной ключ - массив байтов,
    результат - массив раундовых ключей (каждый раундовый ключ - массив байтов))
    """
    @abstractmethod
    def expand_key(self, master_key: bytes) -> List[bytes]:
        pass

