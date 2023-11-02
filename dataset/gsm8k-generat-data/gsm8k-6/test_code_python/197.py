def solution():
    # Calculate the total number of rolls eaten by half the people
    rolls_eaten_by_half = (16 / 2) * (1.5)  # half the people eat 1 1/2 rolls each

    # Calculate the total number of rolls eaten by the other half of the people
    rolls_eaten_by_other_half = (16 / 2) * (0.5)  # other half eat 1/2 roll each

    # Calculate the total number of rolls eaten
    total_rolls_eaten = rolls_eaten_by_half + rolls_eaten_by_other_half

    # Calculate the number of rolls left over
    rolls_left_over = 40 - total_rolls_eaten
    result = rolls_left_over
    return result

print(solution())