def solution():
    
    people = 16
    dinner_rolls = 40
    rolls_eaten_1 = people / 2 * 1.5
    rolls_eaten_2 = people / 2 * 0.5
    total_rolls_eaten = rolls_eaten_1 + rolls_eaten_2
    leftover_rolls = dinner_rolls - total_rolls_eaten
    result = leftover_rolls
    return result

print(solution())