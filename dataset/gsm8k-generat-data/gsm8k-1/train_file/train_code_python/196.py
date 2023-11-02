def solution():
    """There are 16 people at a dinner party. There are 40 dinner rolls available for them. Half the people eat 1 1/2 rolls each. The other half eat 1/2 a roll each. How many dinner rolls are leftover?"""
    num_people = 16
    num_rolls = 40
    rolls_half1 = (num_people // 2) * 1.5
    rolls_half2 = (num_people // 2) * 0.5
    total_rolls = rolls_half1 + rolls_half2
    leftover_rolls = num_rolls - total_rolls
    result = leftover_rolls
    return result

print(solution())