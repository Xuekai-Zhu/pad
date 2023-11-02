def solution():
    # Calculate the height Stephen reached on each round trip
    height_reached = 3/4 * 40000  # Stephen reached 3/4 of the mountain's height on each trip
    
    # Calculate the total distance covered by Stephen
    total_distance = height_reached * 2 * 10  # Stephen made 10 round trips
    
    result = total_distance
    return result

print(solution())