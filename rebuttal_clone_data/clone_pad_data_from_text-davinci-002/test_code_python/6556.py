def solution():
    money = 10
    molds = 3
    popsticks = 1
    juice = 2
    popsicles_made = (money - molds - popsticks) / juice
    sticks_left = popsicles_made % 100
    result = sticks_left
    return result

print(solution())