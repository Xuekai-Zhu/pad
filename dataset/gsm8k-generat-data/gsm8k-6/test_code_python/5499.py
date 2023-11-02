def solution():
    # Calculate the distance traveled by Grayson in his motorboat
    distance_grayson = 25 * 1 + 20 * 0.5  # distance = speed x time
    # Calculate the distance traveled by Rudy in his rowboat
    distance_rudy = 10 * 3  # distance = speed x time
    # Calculate the difference in distance traveled by Grayson and Rudy
    diff_distance = distance_grayson - distance_rudy
    result = diff_distance
    return result

print(solution())