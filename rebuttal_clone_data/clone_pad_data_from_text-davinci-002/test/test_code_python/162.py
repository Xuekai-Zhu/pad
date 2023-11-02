def solution():
    total_sugar = 24
    sugar_per_bag = total_sugar / 4
    lost_sugar = sugar_per_bag / 2
    remaining_sugar = total_sugar - lost_sugar
    result = remaining_sugar
    return result

print(solution())