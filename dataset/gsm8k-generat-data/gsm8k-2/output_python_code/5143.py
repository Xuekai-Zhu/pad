def solution():
    """Johny traveled South 40 miles, then turned East and traveled for 20 more miles than the distance he took to travel to the south. If he turned North and traveled twice the distance he had traveled to the East, calculate the total distance his journey took."""
    south_distance = 40
    east_distance = south_distance + 20
    north_distance = 2 * east_distance
    total_distance = south_distance + east_distance + north_distance
    result = total_distance
    return result

print(solution())