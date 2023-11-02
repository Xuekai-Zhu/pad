def solution():
    cars = 3
    taxis = 6
    vans = 2
    people_in_cars = 4
    people_in_taxis = 6
    people_in_vans = 5
    total_people = cars * people_in_cars + taxis * people_in_taxis + vans * people_in_vans
    result = total_people
    return result

print(solution())