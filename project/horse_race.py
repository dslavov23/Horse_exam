class HorseRace():
    # valid race types
    VALID_RACE_TYPES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, race_type):
        self.__validate_race_type(race_type)
        self.__race_type = race_type

    def __validate_race_type(self, race_type):
        if not isinstance(race_type, str) or race_type not in self.VALID_RACE_TYPES:
            raise ValueError(f"Race type does not exist!")
