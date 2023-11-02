def solution():
    # Define the distance Veronica's flashlight can be seen
    veronica_distance = 1000

    # Define the distance Freddie's flashlight can be seen, three times farther than Veronica's
    freddie_distance = 3 * veronica_distance

    # Define the distance Velma's flashlight can be seen, 2000 less than 5 times farther than Freddie's
    velma_distance = 5 * freddie_distance - 2000

    # Calculate the difference between Velma's and Veronica's distances
    distance_difference = velma_distance - veronica_distance

    result = distance_difference
    return result

print(solution())