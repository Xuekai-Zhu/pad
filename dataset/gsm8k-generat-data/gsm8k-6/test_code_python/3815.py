def solution():
    # Calculate the total distance Richard has already walked
    total_distance_walked = 20 + (1/2)*(20-6) + 10  # Richard walks 20 miles the first day, 6 miles less than half as much the next day, and 10 miles the third day

    # Calculate the distance left for Richard to walk
    distance_left = 70 - total_distance_walked

    result = distance_left
    return result

print(solution())