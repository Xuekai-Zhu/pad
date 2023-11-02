def solution():
    num_birds = 2
    num_round_trips = 10
    distance_per_round_trip = 200

    # Calculate the distance traveled by each bird in one round trip
    bird_distance_per_round_trip = 2 * distance_per_round_trip

    # Calculate the total distance traveled by one bird in all round trips
    bird_total_distance = num_round_trips * bird_distance_per_round_trip

    # Calculate the total distance traveled by both birds in all round trips
    total_distance = num_birds * bird_total_distance
    result = total_distance
    return result

print(solution())