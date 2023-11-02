def solution():
    # Calculate the number of people eating 1 1/2 rolls each
    half_eating_more = 16 // 2
    rolls_eaten_by_half = half_eating_more * 1.5

    # Calculate the number of people eating 1/2 a roll each
    half_eating_less = 16 // 2
    rolls_eaten_by_other_half = half_eating_less * 0.5

    # Total number of rolls eaten
    total_rolls_eaten = rolls_eaten_by_half + rolls_eaten_by_other_half

    # Calculate the number of leftover rolls
    rolls_leftover = 40 - total_rolls_eaten
    result = rolls_leftover
    return result

print(solution())