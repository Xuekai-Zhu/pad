def solution():
    """Stephen made 10 round trips up and down a 40,000 foot tall mountain. If he reached 3/4 of the mountain's height on each of his trips, calculate the total distance he covered."""
    mountain_height = 40000
    trip_height = mountain_height * 0.75
    round_trips = 10
    total_distance = round_trips * 2 * trip_height
    result = total_distance
    return result

print(solution())