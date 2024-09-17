import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        return self.health

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return self.strength

    def battleCry(self):
        return "¡Odin os posee a todos!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} ha perdido {damage} puntos de daño"
        else:
            return f"{self.name} ha muerto en combate"

# Saxon
class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"Un Saxon ha recibido {damage} puntos de daño"
        else:
            return "Un Saxon ha muerto en combate"

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return "No hay suficientes guerreros para combatir"

        # Elegir un Viking y un Saxon al azar
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        # El Saxon recibe daño igual a la fuerza del Viking
        result = saxon.receiveDamage(viking.attack())

        # Eliminar al Saxon si ha muerto
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

        return result

    def saxonAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return "No hay suficientes guerreros para combatir"

        # Elegir un Viking y un Saxon al azar
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        # El Viking recibe daño igual a la fuerza del Saxon
        result = viking.receiveDamage(saxon.attack())

        # Eliminar al Viking si ha muerto
        if viking.health <= 0:
            self.vikingArmy.remove(viking)

        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "¡Los Vikingos han ganado la guerra del siglo!"
        elif len(self.vikingArmy) == 0:
            return "Los Sajones han luchado por sus vidas y sobreviven otro día..."
        else:
            return "Los Vikingos y los Sajones todavía están en plena batalla."
pass


# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass


