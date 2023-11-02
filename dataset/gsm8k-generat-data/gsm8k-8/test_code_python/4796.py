def solution():
    # Define the number of trucks
    num_trucks = 20
    
    # Calculate the number of tanks
    num_tanks = 5 * num_trucks
    
    # Calculate the total number of vehicles
    total_vehicles = num_trucks + num_tanks
    
    result = (num_trucks, num_tanks, total_vehicles)
    return result

print(solution())