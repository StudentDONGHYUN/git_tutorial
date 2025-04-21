class Character:
    def __init__(self, name, basic_attack, skills):
        self.name = name
        self.basic_attack = basic_attack
        self.skills = skills  # {1: dmg, ..., 5: dmg}

    def attack(self):
        return self.basic_attack

    def use_skill(self, level):
        return self.skills.get(level, 0)