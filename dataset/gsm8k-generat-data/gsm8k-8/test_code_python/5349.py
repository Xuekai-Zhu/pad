def solution():
    # Define the distances traveled at each speed
    distance1 = 50 * 3
    distance2 = 80 * 4

    # Calculate the total distance traveled
    total_distance = distance1 + distance2

    # Calculate the remaining distance to the hotel
    remaining_distance = 600 - total_distance
    result = remaining_distance
    return result

print(solution())