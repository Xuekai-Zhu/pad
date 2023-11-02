def solution():
    """A road has four lanes, and in each lane, the number of cars is twice as many as the number of trucks in all the lanes. If there are 60 trucks in each lane, calculate the total number of vehicles in all the lanes?"""
    trucks_per_lane = 60
    cars_per_lane = 2 * trucks_per_lane
    total_vehicles = (trucks_per_lane + cars_per_lane) * 4
    result = total_vehicles
    return result

print(solution())