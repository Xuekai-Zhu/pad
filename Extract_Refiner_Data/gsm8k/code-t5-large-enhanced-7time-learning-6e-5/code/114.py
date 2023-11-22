def solution():
    
    # Define the number of vehicles in each container
    VEHICLES_PER_CONTAINER = 5

    # Define the number of containers on the first day
    first_day_containers = 2

    # Define the total number of vehicles at the port
    total_vehicles = 30

    # Calculate the total number of vehicles in the first day
    first_day_vehicles = first_day_containers * VEHICLES_PER_CONTAINER

    # Calculate the total number of vehicles in the second day
    second_day_vehicles = total_vehicles - first_day_vehicles

    # Calculate the number of containers on the second day
    second_day_containers = second_day_vehicles // VEHICLES_PER_CONTAINER

    # Display the number of containers on the second day
    result = second_day_containers
    return result

print(solution())