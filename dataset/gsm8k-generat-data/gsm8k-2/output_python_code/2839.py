def solution():
    """In a parking lot, there are cars and motorcycles. Each car has 5 wheels (including one spare) and each motorcycle has 2 wheels. There are 19 cars in the parking lot. Altogether all vehicles have 117 wheels. How many motorcycles are at the parking lot?"""
    car_wheels = 5
    motorcycle_wheels = 2
    total_cars = 19
    total_wheels = 117
    car_wheels_count = total_cars * car_wheels
    motorcycle_wheels_count = total_wheels - car_wheels_count
    motorcycle_count = motorcycle_wheels_count / motorcycle_wheels
    result = motorcycle_count
    return result

print(solution())