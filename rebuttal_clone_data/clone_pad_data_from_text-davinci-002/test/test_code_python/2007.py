def solution():
    floors = 12
    full_floors = floors / 2
    half_floors = floors - full_floors
    apartments_per_floor = 10
    people_per_apartment = 4
    people_on_full_floors = full_floors * apartments_per_floor * people_per_apartment
    people_on_half_floors = half_floors * apartments_per_floor * (people_per_apartment / 2)
    total_people = people_on_full_floors + people_on_half_floors
    result = total_people
    return result

print(solution())