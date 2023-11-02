def solution():
    """An alien invades Earth. It abducts 200 people. He returns 80% of the people abducted. After that he takes 10 people to another planet. He took the rest to his home planet. How many people did he take to his home planet?"""
    people_abducted = 200
    returned_people = 0.8 * people_abducted
    taken_to_another_planet = 10
    taken_to_home_planet = people_abducted - returned_people - taken_to_another_planet
    result = taken_to_home_planet
    return result

print(solution())