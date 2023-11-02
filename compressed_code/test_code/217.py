def solution():
    
    total_sugar = 24
    sugar_per_bag = total_sugar / 4
    sugar_lost = sugar_per_bag / 2
    remaining_sugar = total_sugar - sugar_lost
    result = remaining_sugar
    return result

print(solution())