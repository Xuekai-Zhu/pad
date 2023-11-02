def solution():
    # Distance Veronica's flashlight can be seen
    veronica_distance = 1000

    # Distance Freddie's flashlight can be seen
    freddie_distance = 3 * veronica_distance

    # Distance Velma's flashlight can be seen
    velma_distance = (5 * freddie_distance) - 2000

    # Calculate how much farther Velma's flashlight can be seen compared to Veronica's
    difference = velma_distance - veronica_distance
    result = difference
    return result

print(solution())