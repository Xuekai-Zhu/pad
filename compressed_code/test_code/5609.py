def solution():
    
    num_guest_cars = 10
    num_wheels_per_car = 4
    num_dylan_cars = 2
    num_wheels_dylan_cars = num_wheels_per_car * num_dylan_cars
    total_wheels = num_wheels_dylan_cars + (num_guest_cars * num_wheels_per_car)
    result = total_wheels
    return result

print(solution())