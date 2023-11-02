def solution():
    
    total_people = 84
    cars = 7
    per_car_capacity = 2
    total_capacity = cars * per_car_capacity
    rides_needed = total_people // total_capacity
    if total_people % total_capacity != 0:
        rides_needed += 1
    result = rides_needed
    return result

print(solution())