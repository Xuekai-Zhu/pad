def solution():
    """It takes 5 people to lift a car and twice as many people to lift a truck. How many people are needed to lift 6 cars and 3 trucks?"""
    car_lifters = 5
    truck_lifters = 2 * car_lifters
    total_lifters = (6 * car_lifters) + (3 * truck_lifters)
    result = total_lifters
    return result

print(solution())