def solution():
    # Calculate the distance between the first three buoys
    distance_between_buoys = 72 / 2  # There are two intervals between the first three buoys

    # Calculate the distance from the beach to the fourth buoy
    distance_to_fourth_buoy = distance_between_buoys + 72  # Add the distance between buoys to the distance swum to reach the third buoy

    result = distance_to_fourth_buoy
    return result

print(solution())