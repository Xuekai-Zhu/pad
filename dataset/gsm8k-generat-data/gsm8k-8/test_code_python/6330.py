def solution():
    # Define the total distance and distance covered on the first two days
    total_distance = 50
    distance_day1 = 10
    distance_day2 = 0.5 * total_distance

    # Calculate the distance remaining for the third day
    distance_day3 = total_distance - distance_day1 - distance_day2
    result = distance_day3
    return result

print(solution())