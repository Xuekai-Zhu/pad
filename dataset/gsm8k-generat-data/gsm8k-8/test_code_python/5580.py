def solution():
    # Define the cost of a car and a truck in terms of bottle caps
    car_cost = 5
    truck_cost = 6

    # Calculate how many bottle caps Jude spends on trucks
    truck_total_cost = 10 * truck_cost

    # Calculate how many bottle caps Jude has left after buying trucks
    bottle_caps_left = 100 - truck_total_cost

    # Calculate how many bottle caps Jude spends on cars
    car_total_cost = 0.75 * bottle_caps_left

    # Calculate how many cars Jude can buy with the remaining bottle caps
    num_cars = int(car_total_cost / car_cost)

    # Calculate the total number of matchbox vehicles Jude buys
    total_num_vehicles = 10 + num_cars
    result = total_num_vehicles
    return result

print(solution())