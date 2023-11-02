def solution():
    
    people_abducted = 200
    returned_people = 0.8 * people_abducted
    taken_to_another_planet = 10
    taken_to_home_planet = people_abducted - returned_people - taken_to_another_planet
    result = taken_to_home_planet
    return result

print(solution())