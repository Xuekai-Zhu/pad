def solution():
    """Stephen made 10 round trips up and down a 40,000 foot tall mountain. If he reached 3/4 of the mountain's height on each of his trips, calculate the total distance he covered."""
    # Define the height of the mountain and the fraction of height reached on each trip
    mountain_height = 40000
    fraction_reached = 3/4

    # Calculate the total distance covered in one round trip
    round_trip_distance = (2 * fraction_reached * mountain_height)

    # Calculate the total distance covered in all 10 round trips
    total_distance = round_trip_distance * 10

    # return the result
    result = total_distance
    return result

print(solution())