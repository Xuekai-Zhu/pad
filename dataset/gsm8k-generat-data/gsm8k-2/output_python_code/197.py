def solution():
    """There are 16 people at a dinner party. There are 40 dinner rolls available for them. Half the people eat 1 1/2 rolls each. The other half eat 1/2 a roll each. How many dinner rolls are leftover?"""
    total_people = 16
    total_rolls = 40
    half_people = total_people//2
    half_people_x1_5 = half_people * 1.5
    other_half_people = half_people
    other_half_people_x0_5 = other_half_people * 0.5
    total_rolls_used = (half_people_x1_5 + other_half_people_x0_5)
    leftover_rolls = total_rolls - total_rolls_used
    result = leftover_rolls
    return result

print(solution())