def solution():
    # Define number of people needed to lift a car and a truck
    car_lifters = 5
    truck_lifters = car_lifters * 2

    # Calculate total number of people needed to lift 6 cars and 3 trucks
    total_lifters = (car_lifters * 6) + (truck_lifters * 3)
    result = total_lifters
    return result

print(solution())