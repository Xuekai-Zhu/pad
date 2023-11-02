def solution():
    """Wendy's truck has a gas tank that can hold 20 gallons. She also has a car with a gas tank that holds 12 gallons. The truck's tank is half full. The car's tank is 1/3 full. If she fills them both up completely, how many gallons does she add?"""
    truck_tank = 20
    car_tank = 12
    truck_current = truck_tank / 2
    car_current = car_tank / 3
    total_added = (truck_tank - truck_current) + (car_tank - car_current)
    result = total_added
    return result

print(solution())