def solution():
    """There are 16 people at a dinner party. There are 40 dinner rolls available for them. Half the people eat 1 1/2 rolls each. The other half eat 1/2 a roll each. How many dinner rolls are leftover?"""
    people = 16
    dinner_rolls = 40
    rolls_eaten_1 = people / 2 * 1.5
    rolls_eaten_2 = people / 2 * 0.5
    total_rolls_eaten = rolls_eaten_1 + rolls_eaten_2
    leftover_rolls = dinner_rolls - total_rolls_eaten
    result = leftover_rolls
    return result

print(solution())