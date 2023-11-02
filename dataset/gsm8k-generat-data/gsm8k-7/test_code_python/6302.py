def solution():
    num_cars = 125
    regular_cars_percent = 0.64
    truck_percent = 0.08

    # Calculate the number of regular cars
    num_regular_cars = num_cars * regular_cars_percent

    # Calculate the number of truck cars
    num_truck_cars = num_cars * truck_percent
    
    # Calculate the number of convertible cars
    num_convertible_cars = num_cars - num_regular_cars - num_truck_cars
    
    result = num_convertible_cars
    return result

print(solution())