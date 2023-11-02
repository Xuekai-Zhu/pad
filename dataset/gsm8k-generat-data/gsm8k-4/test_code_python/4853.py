def solution():
    """A road has four lanes, and in each lane, the number of cars is twice as many as the number of trucks in all the lanes. If there are 60 trucks in each lane, calculate the total number of vehicles in all the lanes?"""
    # Calculate the total number of trucks in all lanes
    total_trucks = 4 * 60

    # Calculate the total number of cars in all lanes, which is twice the number of trucks
    total_cars = 2 * total_trucks

    # Calculate the total number of vehicles in all lanes
    total_vehicles = total_trucks + total_cars

    # return the result
    result = total_vehicles
    return result

print(solution())