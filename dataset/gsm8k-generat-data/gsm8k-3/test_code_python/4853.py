def solution():
    """A road has four lanes, and in each lane, the number of cars is twice as many as the number of trucks in all the lanes. If there are 60 trucks in each lane, calculate the total number of vehicles in all the lanes?"""
    # Define the number of trucks in each lane
    trucks = 60

    # Calculate the number of cars in each lane
    cars = trucks * 2

    # Calculate the total number of vehicles in all lanes
    total_vehicles = (trucks + cars) * 4

    # Display the total number of vehicles
    result = total_vehicles
    return result

print(solution())