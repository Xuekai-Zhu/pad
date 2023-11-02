def solution():
    num_abducted = 200
    returning_percentage = 0.8
    num_to_other_planet = 10

    # Calculate the number of people returned to Earth
    num_returned = num_abducted * returning_percentage

    # Calculate the number of people not returned
    num_not_returned = num_abducted - num_returned

    # Calculate the number of people taken to the home planet
    num_to_home = num_not_returned - num_to_other_planet

    result = num_to_home
    return result

print(solution())