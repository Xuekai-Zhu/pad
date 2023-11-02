def solution():
    # Calculate the total distance from base camp to chain challenge
    total_distance = 3

    # Calculate the distance covered by each car
    distance_per_car = total_distance / 30

    # Calculate the time taken for each car to cover the distance
    time_per_car = 20 / 60 # convert minutes to hours

    # Calculate the total time taken for 30 cars to come down the road
    total_time = time_per_car * 30

    result = total_time
    return result

print(solution())