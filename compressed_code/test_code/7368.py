def solution():
    
    time_driving_1 = 2 
    speed_1 = 60 
    time_driving_2 = 3 
    speed_2 = 50 
    distance_1 = time_driving_1 * speed_1 
    distance_2 = time_driving_2 * speed_2 
    total_distance = distance_1 + distance_2 
    miles_per_gallon = 30 
    cost_per_gallon = 2 
    gallons_used = total_distance / miles_per_gallon 
    cost_of_gas = gallons_used * cost_per_gallon 
    result = cost_of_gas
    return result

print(solution())