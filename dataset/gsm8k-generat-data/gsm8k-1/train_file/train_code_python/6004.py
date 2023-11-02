def solution():
    """A 25 story building has 4 apartments on each floor. If each apartment houses two people, how many people does the building house?"""
    floors = 25
    apartments_per_floor = 4
    people_per_apartment = 2
    total_people = floors * apartments_per_floor * people_per_apartment
    result = total_people
    return result

print(solution())