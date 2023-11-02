def solution():
    """A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?"""
    # Initialize variables for the number of people on the first ship and the total number of people eaten
    num_people_on_first_ship = 0
    total_people_eaten = 847

    # Calculate the number of people on the first ship by working backwards through time
    for i in range(2, 5):
        num_people_on_current_ship = (total_people_eaten / 2) + 1
        total_people_eaten -= num_people_on_current_ship
        if i == 2:
            num_people_on_first_ship = num_people_on_current_ship

    # return the result
    result = num_people_on_first_ship
    return result

print(solution())