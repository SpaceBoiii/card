class MagicCard():
    def __init__(self, _name, _type, mana, number, effect):
        _name = self.name
        _type = self.cardType
        mana = self.mana
        number = self.number
        effect = self.effect
class CreatureCard():
    def __init__(self, _name, mana, number, hp, atk1, atk2, atk3, atk4):
        _name = self.name
        mana = self.mana
        number = self.number
        hp = self.hp
        atk1 = self.atk1
        atk2 = self.atk2
        atk3 = self.atk3
        atk4 = self.atk4
class Attack():
    def __init__(self, _name, dmg, mana):
        _name = self.name
        dmg = self.dmg
        mana = self.mana
