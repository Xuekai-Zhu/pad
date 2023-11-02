def solution():
    # Calculate the distance traveled during the first 3 hours of driving
    distance_first_leg = 50 * 3

    # Calculate the distance traveled during the next 4 hours of driving
    distance_second_leg = 80 * 4

    # Calculate the total distance traveled
    total_distance = distance_first_leg + distance_second_leg

    # Calculate the distance remaining to reach the hotel
    distance_remaining = 600 - total_distance
    result = distance_remaining
    return result

print(solution())