class Animal:
    """
    The base class representing an animal.

    Attributes:
        name (str): The name of the animal.
        age (int): The age of the animal.
    """

    def __init__(self, name, age):
        """
        Initializes a new instance of the Animal class.

        Args:
            name (str): The name of the animal.
            age (int): The age of the animal.
        """
        self.name = name
        self.age = age

    def make_sound(self):
        """
        This method should be overridden by subclasses to define the sound the animal makes.

        Returns:
            str: A string representing the sound of the animal.
        """
        pass

    def do_trick(self):
        """
        This method should be overridden by subclasses to define a trick the animal can perform.

        Returns:
            str: A string representing the trick performed by the animal.
        """
        pass


class Lion(Animal):
    """
    A class representing a lion, a type of animal.

    Inherits from the Animal class.
    """

    def make_sound(self):
        """
        Generates a string describing the lion's roar.

        Returns:
            str: A string describing the lion's roar.
        """
        return f"{self.name}, the lion, is roaring!"

    def do_trick(self):
        """
        Generates a string describing a giant leap performed by the lion.

        Returns:
            str: A string describing the lion's giant leap.
        """
        return f"{self.name}, the lion, makes a giant leap!"


class Dog(Animal):
    """
    A class representing a dog, a type of animal.

    Inherits from the Animal class.
    """

    def make_sound(self):
        """
        Generates a string describing the dog's bark.

        Returns:
            str: A string describing the dog's bark.
        """
        return f"{self.name}, the dog, is barking!"

    def do_trick(self):
        """
        Generates a string describing the dog catching a ball.

        Returns:
            str: A string describing the dog catching a ball.
        """
        return f"{self.name}, the dog, catches the ball!"


class Elephant(Animal):
    """
    A class representing an elephant, a type of animal.

    Inherits from the Animal class.
    """

    def make_sound(self):
        """
        Generates a string describing the elephant's trumpet.

        Returns:
            str: A string describing the elephant's trumpet.
        """
        return f"{self.name}, the elephant, is trumpeting!"

    def do_trick(self):
        """
        Generates a string describing a prediction made by the elephant.

        Returns:
            str: A string describing the elephant's prediction.
        """
        return f"{self.name}, the elephant, is making predictions!"


if __name__ == "__main__":
    dog = Dog('Cheema', 20)
    elephant = Elephant("Asghar", 2)
    lion = Lion("Nomi Bhai", 22)
    print(lion.make_sound())
    print(elephant.make_sound())
    print(dog.do_trick())
