def solution():
    num_buoys = 4
    distance_to_third_buoy = 72

    # Calculate the distance between the first and third buoys
    distance_between_buoys = distance_to_third_buoy / 3

    # Calculate the distance between the first and fourth buoys
    distance_to_fourth_buoy = distance_between_buoys * 4

    result = distance_to_fourth_buoy
    return result

print(solution())