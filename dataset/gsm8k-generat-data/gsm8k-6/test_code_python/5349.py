def solution():
    # Calculate the distance he drove during the first 3 hours
    distance_first_leg = 50 * 3

    # Calculate the distance he drove during the next 4 hours
    distance_second_leg = 80 * 4

    # Calculate the total distance to the hotel
    total_distance = distance_first_leg + distance_second_leg

    # Calculate the distance remaining to the hotel
    distance_remaining = 600 - total_distance
    result = distance_remaining
    return result

print(solution())