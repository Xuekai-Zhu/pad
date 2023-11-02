def solution():
    """In a parking lot, there are cars and motorcycles. Each car has 5 wheels (including one spare) and each motorcycle has 2 wheels. There are 19 cars in the parking lot. Altogether all vehicles have 117 wheels. How many motorcycles are at the parking lot?"""
    car_wheels = 5
    motorcycle_wheels = 2
    total_vehicles = 19
    total_wheels = 117
    # calculate the number of car wheels
    car_total_wheels = total_vehicles * car_wheels
    # calculate the number of motorcycle wheels
    motorcycle_total_wheels = total_wheels - car_total_wheels
    # calculate the number of motorcycles
    motorcycles = motorcycle_total_wheels // motorcycle_wheels
    result = motorcycles
    return result

print(solution())