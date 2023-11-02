def solution():
    people_in_cars = 5 * 2
    people_in_vans = 3 * 3
    total_people = people_in_cars + people_in_vans
    max_capacity = (6 * 2) + (8 * 3)
    result = max_capacity - total_people
    
    return result

print(solution())