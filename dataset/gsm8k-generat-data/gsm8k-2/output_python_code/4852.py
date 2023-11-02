def solution():
    """A road has four lanes, and in each lane, the number of cars is twice as many as the number of trucks in all the lanes. If there are 60 trucks in each lane, calculate the total number of vehicles in all the lanes?"""
    truck_per_lane = 60
    car_per_lane = 2 * truck_per_lane
    total_vehicles_per_lane = truck_per_lane + car_per_lane
    total_lanes = 4
    total_vehicles = total_lanes * total_vehicles_per_lane
    result = total_vehicles
    return result

print(solution())