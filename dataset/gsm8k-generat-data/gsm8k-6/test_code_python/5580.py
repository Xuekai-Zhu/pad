def solution():
    # Calculate the number of bottle caps used to buy trucks
    caps_for_trucks = 6 * 10  # 6 bottle caps for a truck
    
    # Calculate the number of remaining bottle caps after buying trucks
    remaining_caps = 100 - caps_for_trucks
    
    # Calculate the number of bottle caps used to buy cars
    caps_for_cars = int(0.75 * remaining_caps)  # 75% of remaining bottle caps
    
    # Calculate the number of cars bought with the remaining bottle caps
    cars_bought = int(caps_for_cars / 5)  # 5 bottle caps for a car
    
    # Calculate the total number of matchbox vehicles bought
    total_vehicles = 10 + cars_bought + 10  # 10 trucks and 10 cars already bought
    
    result = total_vehicles
    return result

print(solution())