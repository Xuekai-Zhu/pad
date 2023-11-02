def solution():
    """Stephen made 10 round trips up and down a 40,000 foot tall mountain. If he reached 3/4 of the mountain's height on each of his trips, calculate the total distance he covered."""
    # Define the height of the mountain and the proportion Stephen reached each trip
    MOUNTAIN_HEIGHT = 40000
    PROPORTION_REACHED = 0.75

    # Calculate the height Stephen reached on each trip
    height_reached = MOUNTAIN_HEIGHT * PROPORTION_REACHED

    # Calculate the distance covered on each round trip
    round_trip_distance = height_reached * 2

    # Calculate the total distance covered by Stephen
    total_distance = round_trip_distance * 10

    # Display the total distance covered
    result = total_distance
    return result

print(solution())