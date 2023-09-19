class Handler:
    DEFAULT = 0

    CURRENT = 0

    DIRECTION = None

    def validate_direction(self):
        pass

    def validate_floor(self):
        pass

    def go_to_floor(self, floor):
        print(f"floor {floor} has reached")
        self.CURRENT = floor


class InnerButton:
    INNER = {
        "G": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "Open": 8,
        "Close": 9,
    }

    def __init__(self, button):
        self.button = self.INNER.get(button)

    def pressed(self):
        if self.button:
            floor = 
            return floor


class OuterButton:
    OUTER = {
        "Up": 0,
        "Down": 1,
    }

    def __init__(self, button):
        self.button = button

    def pressed(self):
        if self.button:
            floor = self.OUTER.get(self.button)
            return floor


class Floor:
    pass

if __name__ == '__main__':
    input()

