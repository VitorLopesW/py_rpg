class Item:
    def __init__(self):
        self.disposable = None
    def use(self, player):
        if self.disposable == True:
            player.inventory.remove(self)
        else:
            print(f"{self.name}, can't be used right now!")
        

class Potion(Item):
    def __init__(self):
        super().__init__()
        self.type = 'potion'

class Health_potion(Potion):
    def __init__(self):
        super().__init__()
        self.life_gain = 10
        self.disposable = True
    def use(self, player):
        player.current_hp += self.life_gain
        if player.current_hp > player.hp:
            player.current_hp = player.hp
        super().use(player)
        print(f"{player.name} used a {self.name}, and gained {self.life_gain} hp!")


class Lesser_healing_potion(Health_potion):
    def __init__(self):
        super().__init__()
        self.name = 'Lesser Healing Potion'
        self.description = 'A small red potion, that heals 5 hp' 
        self.life_gain = 5
    def use(self, player):
        super().use(player)
