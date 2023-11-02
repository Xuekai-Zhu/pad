def solution():
    round_trips_per_bird = 10  # Each bird made 10 round trips
    distance_per_round_trip = 2 * 200  # The distance to the building materials and back is 200 miles each way

    # Calculate the total distance covered by both birds
    total_distance = 2 * round_trips_per_bird * distance_per_round_trip
    result = total_distance
    return result

print(solution())