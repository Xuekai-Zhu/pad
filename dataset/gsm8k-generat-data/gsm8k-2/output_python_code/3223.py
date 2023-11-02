def solution():
    """Stephen rides his bicycle to church. During the first third of his trip, he travels at a speed of 16 miles per hour. During the second third of his trip, riding uphill, he travels a speed of 12 miles per hour. During the last third of his trip, he rides downhill at a speed of 20 miles per hour. If each third of his trip takes 15 minutes, what is the distance Stephen rides his bicycle to church, in miles?"""
    time_per_third = 0.25 # 15 minutes
    distance_per_third = 0
    
    # first third of the trip
    speed = 16
    time = time_per_third
    distance = speed * time
    distance_per_third += distance
    
    # second third of the trip
    speed = 12
    time = time_per_third
    distance = speed * time
    distance_per_third += distance
    
    # last third of the trip
    speed = 20
    time = time_per_third
    distance = speed * time
    distance_per_third += distance
    
    total_distance = distance_per_third * 3
    result = total_distance
    return result

print(solution())