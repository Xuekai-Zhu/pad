def solution():
    
    walk_time = 2 
    bike_time = 1 
    walk_frequency = 3 
    bike_frequency = 2 
    total_walk_time = walk_time * 2 * walk_frequency 
    total_bike_time = bike_time * 2 * bike_frequency 
    total_time = total_walk_time + total_bike_time
    result = total_time
    return result

print(solution())