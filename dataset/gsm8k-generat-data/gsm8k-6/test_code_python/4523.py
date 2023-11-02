def solution():
    # Calculate the number of people returned to Earth
    returned_people = 200 * 0.8

    # Calculate the number of people taken to the other planet
    other_planet_people = 10

    # Calculate the number of people taken to the alien's home planet
    home_planet_people = 200 - returned_people - other_planet_people
    result = home_planet_people
    return result

print(solution())