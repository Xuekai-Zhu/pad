def solution():
    """Jenna is on a road trip. She drives for 2 hours at 60mph. She takes a bathroom break, and then she continues driving for 3 hours at 50 mph. She can drive for 30 miles on one gallon of gas. If one gallon of gas costs $2, how much money does she spend on gas for her trip?"""
    time_driving_1 = 2 # hours
    speed_1 = 60 # miles per hour
    time_driving_2 = 3 # hours
    speed_2 = 50 # miles per hour
    distance_1 = time_driving_1 * speed_1 # miles
    distance_2 = time_driving_2 * speed_2 # miles
    total_distance = distance_1 + distance_2 # miles
    miles_per_gallon = 30 # miles per gallon
    cost_per_gallon = 2 # dollars per gallon
    gallons_used = total_distance / miles_per_gallon # gallons
    cost_of_gas = gallons_used * cost_per_gallon # dollars
    result = cost_of_gas
    return result

print(solution())