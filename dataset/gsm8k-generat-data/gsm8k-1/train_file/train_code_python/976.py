def solution():
    """Tommy goes for a run around his neighborhood and decides to calculate how many wheels he saw. All the trucks in his neighborhood have 4 wheels and all the cars in his neighborhood also have 4 wheels. If he saw 12 trucks and 13 cars, how many wheels did he see?"""
    trucks = 12
    cars = 13
    wheels_per_vehicle = 4
    total_wheels = (trucks + cars) * wheels_per_vehicle
    result = total_wheels
    return result

print(solution())