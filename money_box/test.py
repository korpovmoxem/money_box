class MoneyDay:
    day_number = 1

    def __init__(self, value=0):
        self.day_number = MoneyDay.day_number
        self.value = value
        MoneyDay.day_number += 1


def create_table(goal):
    l = []
    temp = 20
    s = 0
    for i in range(100):
        l.append(MoneyDay(value=temp))
        temp += 20
    for i in l:
        s += i.value
    if s > goal:
        m = s - goal
        