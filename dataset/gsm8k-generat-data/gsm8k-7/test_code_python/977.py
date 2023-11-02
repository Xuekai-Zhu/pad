def solution():
    num_trucks = 12
    num_cars = 13
    wheels_per_truck = 4
    wheels_per_car = 4

    # Calculate the total number of wheels from trucks
    total_truck_wheels = num_trucks * wheels_per_truck

    # Calculate the total number of wheels from cars
    total_car_wheels = num_cars * wheels_per_car

    # Calculate the total number of wheels Tommy saw
    total_wheels = total_truck_wheels + total_car_wheels
    result = total_wheels
    return result

print(solution())