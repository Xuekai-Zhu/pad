def solution():
    """Stephen made 10 round trips up and down a 40,000 foot tall mountain. If he reached 3/4 of the mountain's height on each of his trips, calculate the total distance he covered."""
    trips = 10
    mountain_height = 40000
    distance_covered_per_trip = 3/4 * mountain_height * 2
    total_distance_covered = trips * distance_covered_per_trip
    result = total_distance_covered
    return result

print(solution())