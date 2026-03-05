# Write code below 💖
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name)
        print(self.name)

    def display_details(self):
        print(f"Entry number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")

        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught.")


Pikachu = Pokemon(
    25,
    "Pikachu",
    "Electric",
    "It has small electric sacs on both its cheeks. If threatened, it loses electric charges from the sacs.", True)

Pikachu.speak()
Pikachu.display_details()

Bulbasaur = Pokemon(1, 'Bulbasaur', 'seed',
                    'For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.', True)

Bulbasaur.speak()
Bulbasaur.display_details()
