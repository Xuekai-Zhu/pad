def solution():
    """Wendy's truck has a gas tank that can hold 20 gallons. She also has a car with a gas tank that holds 12 gallons. 
    The truck's tank is half full. The car's tank is 1/3 full. If she fills them both up completely, how many gallons does she add?"""
    truck_half_tank = 20 / 2
    car_one_third_tank = 12 / 3
    total_gallons_added = (20 - truck_half_tank) + (12 - car_one_third_tank)
    result = total_gallons_added
    return result

print(solution())