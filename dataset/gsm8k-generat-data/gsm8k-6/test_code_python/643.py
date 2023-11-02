def solution():
    # Calculate the maximum distance each flashlight can be seen
    veronica_distance = 1000
    freddie_distance = 3 * veronica_distance
    velma_distance = (5 * freddie_distance) - 2000

    # Calculate the difference in distance between Velma's and Veronica's flashlights
    distance_difference = velma_distance - veronica_distance
    result = distance_difference
    return result

print(solution())