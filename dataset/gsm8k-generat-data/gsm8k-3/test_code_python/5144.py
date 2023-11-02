def solution():
    """Johny traveled South 40 miles, then turned East and traveled for 20 more miles than the distance he took to travel to the south. If he turned North and traveled twice the distance he had traveled to the East, calculate the total distance his journey took."""
    # Define the distance traveled to the south
    south_distance = 40

    # Define the distance traveled to the east
    east_distance = south_distance + 20

    # Define the distance traveled to the north
    north_distance = east_distance * 2

    # Calculate the total distance traveled
    total_distance = south_distance + east_distance + north_distance

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())