def solution():
    """A party hall has 3 decorative light bulbs; a red light bulb which comes on every 2 seconds, a green one every 3 seconds and a blue one every 4 seconds. If they are put on at the same time, what is the shortest time after which the three bulbs will be on at the same time?"""
    # Define the periods of the light bulbs
    red_period = 2
    green_period = 3
    blue_period = 4

    # Initialize the time counter
    time = 0

    # Check if the three bulbs are on at the same time
    while True:
        if time % red_period == 0 and time % green_period == 0 and time % blue_period == 0:
            break
        time += 1

    result = time
    return result

print(solution())