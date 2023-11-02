def solution():
    num_cars = 15
    num_bicycles = 3
    num_trucks = 8
    num_tricycles = 1
    tires_per_car = 4
    tires_per_bicycle = 2
    tires_per_truck = 4
    tires_per_tricycle = 3
    
    # Calculate the total number of tires on cars
    total_car_tires = num_cars * tires_per_car
    
    # Calculate the total number of tires on bicycles
    total_bicycle_tires = num_bicycles * tires_per_bicycle
    
    # Calculate the total number of tires on trucks
    total_truck_tires = num_trucks * tires_per_truck
    
    # Calculate the total number of tires on tricycles
    total_tricycle_tires = num_tricycles * tires_per_tricycle
    
    # Calculate the total number of tires on all vehicles
    total_tires = total_car_tires + total_bicycle_tires + total_truck_tires + total_tricycle_tires
    result = total_tires
    return result

print(solution())