def solution():
    """Tommy goes for a run around his neighborhood and decides to calculate how many wheels he saw. All the trucks in his neighborhood have 4 wheels and all the cars in his neighborhood also have 4 wheels. If he saw 12 trucks and 13 cars, how many wheels did he see?"""
    truck_wheels = 4
    car_wheels = 4
    num_trucks = 12
    num_cars = 13
    total_wheels = (num_trucks * truck_wheels) + (num_cars * car_wheels)
    result = total_wheels
    return result

print(solution())