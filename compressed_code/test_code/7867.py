def solution():
    
    cars = 2
    car_capacity = 6
    vans = 3
    van_capacity = 8
    car_passengers = 5
    van_passengers = 3
    total_passengers = cars * car_passengers + vans * van_passengers
    max_capacity = cars * car_capacity + vans * van_capacity
    remaining_capacity = max_capacity - total_passengers
    result = remaining_capacity
    return result

print(solution())