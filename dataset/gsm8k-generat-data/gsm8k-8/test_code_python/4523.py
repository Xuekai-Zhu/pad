def solution():
    # Calculate the number of people who were returned
    returned_people = 0.8 * 200

    # Calculate the number of people who were taken to another planet
    other_planet_people = 10

    # Calculate the number of people who were taken to the alien's home planet
    home_planet_people = 200 - returned_people - other_planet_people
    result = home_planet_people
    return result

print(solution())