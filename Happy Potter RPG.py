class Wizard:
    def __init__(self, name, health, defense, spells):
        self.health = health
        self.defense = defense
        self.spells = spells
        self.name = name

    def fight(self, otherWizard):
        damage = self.spells - otherWizard.defense
        if damage < 0:
            damage = 0
        otherWizard.health = otherWizard.health - damage
        print(self.name + " attacks " + otherWizard.name + " for " + str(damage) + " damage!")


class HarryPotter(Wizard):
    def __init__(self, name, health, defense, spells, speical_ability):
        super().__init__(name, health, defense, spells)
        self.weapon = None
        self.potions = 3
        self.speical_ability = speical_ability

    def selectWeapon(self):
        userChoice = int(input("Select a Weapon: 1) Sword, 2) Wand"))
        if userChoice == 1:
            self.weapon = "Sword"
            self.spells += 3
            self.spells += 3
        else:
            self.weapon = "Wand"
            self.spells += 5

    def heal(self):
        if self.potions > 0:
            self.health += 30
            self.potions -= 1
            print("You drank a potion and healed for 10 hit points!")
            print("Your current health is: " + str(self.health))
        else:
            print("You're out of potions!")

    def ability(self):
        if self.potions > 0:
            self.health += 30
            self.speical_ability == 20
            print("Harry used Cruciatus! " + str(Voldemort.health))
        else:
            print("Harry can not use his ability")

# Setting up new Objects
# Player Character
myCharacter = HarryPotter("Harry Potter", 50, 5, 15)
myCharacter.selectWeapon()


# CPU Villian
Voldemort = Wizard("Voldemort", 100, 5, 15)

print("A " + Voldemort.name + " stands before you!")
while myCharacter.health >= 0 and Voldemort.health >= 0:
    userChoice = int(input("Would you like to attack[1] or heal?[2]"))
    if userChoice == 1:
        myCharacter.fight(Voldemort)
    else:
        myCharacter.heal()

    Voldemort.fight(myCharacter)
    print(myCharacter.name + " has " + str(myCharacter.health) + "health remaining!")
    print(Voldemort.name + " has " + str(Voldemort.health) + "health remaining!")
