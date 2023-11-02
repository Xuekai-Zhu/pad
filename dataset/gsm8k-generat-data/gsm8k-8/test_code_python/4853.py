def solution():
    # Calculate the total number of trucks in all lanes
    total_trucks = 4 * 60

    # Calculate the total number of vehicles in all lanes (2 cars for every truck)
    total_vehicles = total_trucks * 2

    result = total_vehicles
    return result

print(solution())