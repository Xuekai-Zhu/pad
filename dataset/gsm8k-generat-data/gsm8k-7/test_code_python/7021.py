def solution():
    road_length = 3
    time_per_car = 20/60  # 20 minutes converted to hours
    num_cars = 30

    # Calculate the total time it takes for 30 cars to come down the road
    total_time = time_per_car * num_cars

    # Calculate the number of hours that have passed
    num_hours = total_time / 60

    result = num_hours
    return result

print(solution())