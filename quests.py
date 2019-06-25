import random

class Quest:
    def __init__(self, mainloop):
        self.mainloop = mainloop
        self.completed = False


    def run(self):
        self.completed = mainloop()



def check_number():
    import random

    rand = random.randint(0, 50)
    x = int(input("Podaj liczbę"))
    print(rand)

    while x != rand:
        if x > rand:
            print("Za duża liczba")
        else:
            print("Za mala liczba")

        x = int(input("Podaj kolejną liczbę: "))

def roll_the_dice():
    min = 1
    max = 6

    roll_again = "tak"

    while roll_again == "tak" or roll_again == "y":
        print("Wykonuje rzut...")
        print("Kosci pokazuja...")
        x = random.randint(min, max)
        y = random.randint(min, max)
        print(x)
        print(y)

        if x == y:
            print("Taki sam wynik")
            break
        elif x > y:
            print("Rozne wyniki")
            roll_again = input("Czy chcesz rzucic jeszcze raz?")


