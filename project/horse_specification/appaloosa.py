from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAINING_GAIN = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def type(self):
        return "Appaloosa"
