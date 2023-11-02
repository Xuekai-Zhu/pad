def solution():
    """On a highway, the total number of vehicles passing is 300. If the number of cars on the highway is twice the number of trucks, find out the total number of trucks on the highway?"""
    # Define the total number of vehicles
    total_vehicles = 300

    # Define the ratio of cars to trucks
    car_to_truck_ratio = 2

    # Calculate the total number of trucks
    total_trucks = total_vehicles / (car_to_truck_ratio + 1)

    # Display the total number of trucks
    result = total_trucks
    return result

print(solution())