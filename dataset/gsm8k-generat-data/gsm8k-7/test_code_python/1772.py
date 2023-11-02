def solution():
    distance_north = 55
    distance_west = 95
    speed = 25

    # Calculate the total distance traveled
    total_distance = (distance_north**2 + distance_west**2)**0.5

    # Calculate the total time taken to travel
    total_time = total_distance / speed
    result = total_time
    return result

print(solution())