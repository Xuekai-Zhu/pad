def solution():
    jude_caps = 100
    car_cost = 5
    truck_cost = 6

    # Calculate the total cost of all trucks that Jude will buy
    num_trucks = 10
    total_truck_cost = num_trucks * truck_cost

    # Calculate the number of bottle caps Jude will have left after buying trucks
    jude_caps = jude_caps - total_truck_cost

    # Calculate the total cost of all cars that Jude will buy with 75% of his remaining bottle caps
    num_cars = jude_caps // car_cost
    total_car_cost = num_cars * car_cost

    # Calculate the total number of matchbox vehicles that Jude will buy
    total_matchbox_vehicles = num_trucks + num_cars
    result = total_matchbox_vehicles
    return result

print(solution())