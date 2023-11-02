def solution():
    sugar_per_bag = 24 / 4 # divide the sugar equally among 4 bags
    sugar_lost = sugar_per_bag / 2 # half of the sugar from one bag is lost
    remaining_sugar = (sugar_per_bag * 3) - sugar_lost # the remaining sugar is from the other 3 bags minus the lost sugar
    result = remaining_sugar
    return result

print(solution())