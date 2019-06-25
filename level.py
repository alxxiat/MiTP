from quests import *
import quests
from enemy import *
import functools

class Level:
    def __init__(self, rooms, floor):
        self.rooms = rooms
        self.floor = floor

    def can_move(self, x,y):
        if x in [0,1] and y in [0,1,2]:
            return True
        return False

    def print_map(self, x, y):
       for row in self.rooms:
            print(repr(row[0]) + '\t' + repr(row[1]))

    def is_cleared(self):
        rooms_with_quest = []
        for row in self.rooms:
            for room in row:
                if room.quest is not None:
                    rooms_with_quest.append(room)

        is_cleared = True

        print(rooms_with_quest)

        for room in rooms_with_quest:
            print(room.quest.completed)
            is_cleared = is_cleared and room.quest.completed
        return is_cleared

class Room:
    def __init__(self, name, desc, x, y, items, quest, enemy):
        self.name = name
        self.desc = desc
        self.x = x
        self.y = y
        self.items = items
        self.quest = quest
        self.enemy = enemy


    def __str__(self):
        return self.name + ' - ' + self.desc.lower()

    def __repr__(self):
        return self.name

    def enter(self):
        print(self.desc)


def level_generator(number_of_levels):
    levels = []
    rooms_1 = open("rooms_1.txt", 'r', encoding='utf8')
    rooms_2 = open("rooms_2.txt", 'r', encoding='utf8')
    rooms_3 = open("rooms_3.txt", 'r', encoding='utf8')
    for i in range(number_of_levels):
        if i == 0:
            rooms = room_generator(rooms_1, i + 1)
            levels.append(Level(rooms, i + 1))
            print(rooms)
        if i == 1:
            rooms = room_generator(rooms_2, i + 1)
            levels.append(Level(rooms, i + 1))
            print(rooms)
        if i == 2:
            rooms = room_generator(rooms_3, i + 1)
            levels.append(Level(rooms, i + 1))
            print(rooms)

    rooms_1.close()
    rooms_2.close()
    rooms_3.close()
    return levels


def room_generator(rooms_d, lvl_no):
    rooms_out = []

    if lvl_no == 1:
        for i in range(2):
            rooms_in = []
            for j in range(2):
                rooms_desc = (rooms_d.readline().rstrip(), rooms_d.readline().rstrip())
                if i == 2 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(quests.roll_the_dice), Enemy(
                            "troll", {"health": 100, "attack": 10}
                        )))

            else:
                rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [],None, None))

        rooms_out.append(rooms_in)

    if lvl_no == 2:
        for i in range(3):
            rooms_in = []
            for j in range(2):
                rooms_desc = (rooms_d.readline().rstrip(), rooms_d.readline().rstrip())
                print(rooms_desc)
                if i == 2 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(quests.check_number), Enemy("troll", {"health": 100, "strength": 10})))
                else: rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], None, None))

                rooms_out.append(rooms_in)

    if lvl_no == 3:
        for i in range(3):
            rooms_in = []
            for j in range(2):
                rooms_desc = (rooms_d.readline().rstrip(), rooms_d.readline().rstrip())
                if i == 2 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(quests.check_number),
                                         Enemy("troll", {"health": 100, "strength": 10})))
                else:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], None, None))

                rooms_out.append(rooms_in)

    return rooms_out

