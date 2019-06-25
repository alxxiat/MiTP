from player import *
from level import *



class Game:
    def __init__(self, levels, player):
        self.levels = levels
        self.player = player
        self.current_level = 0


    def run(self):
        while self.player.is_alive():

            self.print_info()
            command = input().lower()
            self.cli(command)

        print("Nie zyjesz")

    def print_info(self):

            print("You're in room", self.player.level.rooms[self.player.y][self.player.x])
            print("[n] Go north")
            print("[s] Go south")
            print("[e] Go east")
            print("[w] Go west")
            print("[map] Show map")
            print("[desc] Print room descriptions")
            print("[level]Go to the next level")

    def cli(self, command):

            command = input().lower()

            if command == "n":
                self.player.move(command)
            elif command == "s":
                self.player.move(command)
            elif command == "e":
                self.player.move(command)
            elif command == "w":
                self.player.move(command)
            elif command == "kill":
                self.player.stats = {"health": 0}
            elif command == 'map':
                self.player.level.print_map(0,0)

            elif command == 'level':

                if self.player.level.is_cleared():
                    self.current_level += 1
                    self.player.level = self.levels[self.current_lvl]
                    self.player.x = 0
                    self.player.y = 2
                else:
                    print("Nie ukończyłeś wszystkich zadań na tym poziomie! ")

            elif command == "quest":
                self.player.level.rooms[self.player.y][self.player.x].quest.run()

            elif command == "fight":
                enemy = self.player.level.rooms[self.player.y, self.player.x].enemy
                if enemy is not None:
                    while self.player.is_alive() and enemy.is_alive():
                        attack_cmd = input("Wybierz rodzaj ataku: \n   --> magiczny \n     --> fizyczny lub wpisz heal aby wyzdrowieć")
                        if attack_cmd == 'heal':
                            self.player.stats["health"] += 50
                        else:
                            self.player.attack(enemy, attack_cmd)
                            enemy.attack(self.player)
                        if not enemy.is_alive():
                            print("Pokonałeś przeiwnika")
                    else:
                        print("W tym pokoju nie ma przeciwnika")
                else:
                    print("Złe polecenie")




def main():
    print("Piec lat temu miasto Tonico dopadla zaraza. \n Niemal wszyscy mieszkancy miasta zgineli w meczarniach lub uciekli szukac schronienia w sasiednich krolestwach. \n "
          "Tylko jeden smialek postanowil powrocic do ruin miasta i zbadac przyczyne tej tragedii.")
    print("Welcome to Tonico. Whats your name?: ")
    name = input()
    levels = level_generator(3)
    player = Player(name, 0, 2, {"health": 10, "strenght":10, "speed": 10}, levels[0])
    game = Game(levels, player)
    game.run()



if __name__ == "__main__":
    main()

def movement_controller(x, y):
    pass
