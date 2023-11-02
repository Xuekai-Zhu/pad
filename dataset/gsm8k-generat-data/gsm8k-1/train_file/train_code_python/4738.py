def solution():
    """On a highway, the total number of vehicles passing is 300. If the number of cars on the highway is twice the number of trucks, find out the total number of trucks on the highway?"""
    total_vehicles = 300
    cars_to_trucks_ratio = 2
    total_ratio_parts = cars_to_trucks_ratio + 1
    trucks = total_vehicles / total_ratio_parts
    result = trucks
    return result

print(solution())