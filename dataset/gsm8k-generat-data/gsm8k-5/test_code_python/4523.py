def solution():
    # Calculate the number of people returned to Earth
    returned_people = 200 * 0.8

    # Subtract the returned people and the 10 taken to another planet from the total number of people abducted
    people_home_planet = 200 - returned_people - 10
    result = people_home_planet
    return result

print(solution())