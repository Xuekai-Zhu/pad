def solution():
    # Calculate the total number of people needed to lift 6 cars and 3 trucks
    car_lifters = 5  # number of people needed to lift one car
    truck_lifters = 2 * car_lifters  # number of people needed to lift one truck
    total_lifters = 6 * car_lifters + 3 * truck_lifters  # number of people needed to lift 6 cars and 3 trucks
    result = total_lifters
    return result

print(solution())