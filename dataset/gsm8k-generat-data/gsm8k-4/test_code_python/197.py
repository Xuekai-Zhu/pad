def solution():
    """There are 16 people at a dinner party. There are 40 dinner rolls available for them. Half the people eat 1 1/2 rolls each. The other half eat 1/2 a roll each. How many dinner rolls are leftover?"""
    # Define the number of people and dinner rolls
    num_people = 16
    num_rolls = 40

    # Calculate the number of rolls eaten by half the people
    rolls_half = (num_people / 2) * 1.5

    # Calculate the number of rolls eaten by the other half
    rolls_other_half = (num_people / 2) * 0.5

    # Calculate the total number of rolls eaten
    rolls_total = rolls_half + rolls_other_half

    # Calculate the number of leftover rolls
    rolls_leftover = num_rolls - rolls_total

    result = rolls_leftover
    return result

print(solution())