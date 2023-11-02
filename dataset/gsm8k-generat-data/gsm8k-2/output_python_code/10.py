def solution():
    """A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?"""
    total_people = 847
    third_ship = total_people / 2 / 2
    second_ship = third_ship * 2
    first_ship = second_ship * 2
    result = first_ship
    return result

print(solution())