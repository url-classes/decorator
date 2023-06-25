from abc import ABCMeta, abstractmethod


class Character(metaclass=ABCMeta):
    @abstractmethod
    def get_life_points(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def calculate_damage(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def receive_damage(self, damage: float):
        raise NotImplementedError
