def solution():
    people_per_car = 5
    people_per_truck = people_per_car * 2
    total_cars = 6
    total_trucks = 3
    total_people = total_cars * people_per_car + total_trucks * people_per_truck
    result = total_people
    return result

print(solution())