def solution():
    
    car_capacity = 4
    taxi_capacity = 6
    van_capacity = 5
    num_cars = 3
    num_taxis = 6
    num_vans = 2
    total_people = num_cars * car_capacity + num_taxis * taxi_capacity + num_vans * van_capacity
    result = total_people
    return result

print(solution())