def solution():
    emus_per_pen = 6 # Each pen has 6 emus
    pens = 4 # John has 4 pens
    emus = emus_per_pen * pens # John has a total of 24 emus
    females = emus/2 # Half of the emus are female
    eggs_per_day = females # Each female emu lays one egg per day
    eggs_per_week = eggs_per_day * 7 # John gets eggs from each female emu every day of the week

    result = eggs_per_week
    return result

print(solution())