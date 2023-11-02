def solution():
    # Define the average distance swung per second
    distance_per_second = 1.2
    
    # Convert 30 minutes to seconds
    time_in_seconds = 30 * 60
    
    # Calculate the total distance swung in meters
    total_distance = distance_per_second * time_in_seconds
    
    result = total_distance
    return result

print(solution())