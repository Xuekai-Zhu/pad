def solution():
    """There are 16 people at a dinner party. There are 40 dinner rolls available for them. Half the people eat 1 1/2 rolls each. The other half eat 1/2 a roll each. How many dinner rolls are leftover?"""
    # Define the total number of dinner rolls and people
    total_rolls = 40
    total_people = 16

    # Calculate the number of rolls eaten by half the people
    half_people_rolls = (total_people/2) * 1.5

    # Calculate the number of rolls eaten by the other half of the people
    other_half_people_rolls = (total_people/2) * 0.5

    # Calculate the total number of rolls eaten
    total_rolls_eaten = half_people_rolls + other_half_people_rolls

    # Calculate the number of leftover rolls
    leftover_rolls = total_rolls - total_rolls_eaten

    # return the result
    result = leftover_rolls
    return result

print(solution())