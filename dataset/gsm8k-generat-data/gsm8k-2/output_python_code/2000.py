def solution():
    """Jenna is on a road trip. She drives for 2 hours at 60mph. She takes a bathroom break, and then she continues driving for 3 hours at 50 mph. She can drive for 30 miles on one gallon of gas. If one gallon of gas costs $2, how much money does she spend on gas for her trip?"""
    distance_1 = 2 * 60
    distance_2 = 3 * 50
    total_distance = distance_1 + distance_2
    gallons_used = total_distance / 30
    cost_per_gallon = 2
    total_cost = gallons_used * cost_per_gallon
    result = total_cost
    return result

print(solution())