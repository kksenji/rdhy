class Character:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality

    def introduce(self):
        print(f"I am {self.name}, and I am {self.personality}")

    def speak(self, dialogue):
        print(f"{self.name} says: {dialogue}")

class Ability:
    def __init__(self, ability_name):
        self.ability_name = ability_name


    def use_ability(self):
        print(f"He has ability {self.ability_name} ")



class AnimeCharacter(Character, Ability):
    def __init__(self, name, personality, ability_name,  anime_name):
        Character.__init__(self, name, personality)
        Ability.__init__(self, ability_name)
        self.anime_name = anime_name

    def watch_anime(self):
        print(f"{self.name} is from {self.anime_name}")

    def special_attack(self):
        print(f"{self.name} is using a special attack!")


anime_character = AnimeCharacter(name="Luffy", personality="Stupid", ability_name="devil fruit hito hito no mi model Nika", anime_name="One Piece")
anime_character.introduce()
anime_character.use_ability()
anime_character.watch_anime()
anime_character.special_attack()
