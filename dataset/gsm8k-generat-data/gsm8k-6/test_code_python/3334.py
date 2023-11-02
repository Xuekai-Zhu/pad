def solution():
    total_animals = 5 + 7  # total number of animals in the ratio
    goats_ratio = 5 / total_animals  # ratio of goats
    sheep_ratio = 7 / total_animals  # ratio of sheep
    total_sheep = sheep_ratio * 360  # total number of sheep on the farm
    total_goats = goats_ratio * 360  # total number of goats on the farm
    goats_sold = total_goats / 2  # number of goats sold
    sheep_sold = total_sheep * (2/3)  # number of sheep sold
    goats_money = goats_sold * 40  # money made from selling goats
    sheep_money = sheep_sold * 30  # money made from selling sheep
    total_money = goats_money + sheep_money  # total money made
    result = total_money
    return result

print(solution())