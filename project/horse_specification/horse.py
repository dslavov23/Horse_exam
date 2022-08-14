import abc

class Horse(abc.ABC):
    # minimum length of name
    MIN_LEN = 4
    # max speed
    MAX_SPEED = None
    # training gain
    TRAINING_GAIN = None

    # the init class
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__validate_name(name)
        self.__name = name

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__validate_speed(speed)
        self.__speed = speed

    def __validate_name(self, value):
        if not isinstance(value, str) or len(value.strip()) < self.MIN_LEN:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

    def __validate_speed(self, value):
        if not isinstance(value, int) or value > self.MAX_SPEED:
            raise ValueError("Horse speed is too high!")

    def train(self):
        # calculate new speed
        _new_speed = self.speed + self.TRAINING_GAIN
        # can not exceed max speed
        if _new_speed >= self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            # else assign new speed
            self.speed = _new_speed

    @property
    @abc.abstractmethod
    def type(self):
        pass
