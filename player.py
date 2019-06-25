import fighting_controller

class Player:
    def __init__(self, name, x, y, stats,level):
        self.name = name
        self.x = x
        self.y = y
        self.stats = stats
        self.inv = []
        self.level = level

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.stats["health"] > 0

    def move(self, direction):
        x_tmp = self.x
        y_tmp = self.y
        if direction == "n":
            y_tmp -= 1
        if direction == "s":
            y_tmp += 1
        if direction == "e":
            x_tmp += 1
        if direction == "w":
            x_tmp -= 1
        if self.level.can_move(x_tmp, y_tmp):
            self.x = x_tmp
            self.y = y_tmp
        else:
            print("You can't move here")

    def attack(self, target, attack_type = "physical"):
        fighting_controller.fighting_controller(self, target, attack_type)


class Item:
    def __init__(self, name):
        self.name = name