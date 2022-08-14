class Jockey():
    # minimum age
    MIN_AGE = 18

    # the init class
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__validate_name(name)
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__validate_age(age)
        self.__age = age

    @staticmethod
    def __validate_name(value):
        if not isinstance(value, str) or len(value.strip()) < 1:
            raise ValueError("Name should contain at least one character!")

    def __validate_age(self, value):
        if not isinstance(value, int) or value < self.MIN_AGE:
            raise ValueError(
                "Jockeys must be at least 18 to participate in the race!")
