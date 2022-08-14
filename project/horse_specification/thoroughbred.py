from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TRAINING_GAIN = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def type(self):
        return "Thoroughbred"
