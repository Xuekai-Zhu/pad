def solution():
    
    walk_time = 2
    bike_time = 1
    num_walks = 3
    num_bikes = 2
    total_walk_time = walk_time * 2 * num_walks
    total_bike_time = bike_time * 2 * num_bikes
    total_time = total_walk_time + total_bike_time
    result = total_time
    return result

print(solution())