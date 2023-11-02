def solution():
    """A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?"""
    # Initialize the total number of people eaten and the number of people on the first ship
    total_eaten = 847
    first_ship = None

    # Calculate the number of people on the third ship (largest)
    third_ship = total_eaten

    # Calculate the number of people on the second ship
    second_ship = third_ship / 2

    # Calculate the number of people on the first ship
    first_ship = second_ship / 2

    result = first_ship
    return result

print(solution())