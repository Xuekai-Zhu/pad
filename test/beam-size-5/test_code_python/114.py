def solution():
    
    # Define the number of vehicles in each container and the total number of vehicles
    VEHICLES_PER_CONTAINER = 5
    TOTAL_VEHICLES = 30

    # Calculate the number of imported vehicles on the first day
    imported_vehicles_first_day = 2 * VEHICLES_PER_CONTAINER

    # Calculate the number of imported vehicles on the second day
    imported_vehicles_second_day = TOTAL_VEHICLES - imported_vehicles_first_day

    # Display the number of imported vehicles on the second day
    result = imported_vehicles_second_day
    return result

print(solution())