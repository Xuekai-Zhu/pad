def solution():
    """A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?"""
    total_consumed = 847
    third_hundred = total_consumed
    second_hundred = third_hundred / 2
    first_hundred = second_hundred / 2
    result = first_hundred
    return result

print(solution())