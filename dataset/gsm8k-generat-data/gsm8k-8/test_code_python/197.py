def solution():
    # Find the number of people eating 1 1/2 rolls each
    half_people = 16 // 2
    rolls_for_half = half_people * 1.5

    # Find the number of people eating 1/2 roll each
    other_half_people = 16 - half_people
    rolls_for_other_half = other_half_people * 0.5

    # Find the total number of rolls needed
    total_rolls = rolls_for_half + rolls_for_other_half

    # Find the number of rolls leftover
    rolls_leftover = 40 - total_rolls
    result = rolls_leftover
    return result

print(solution())