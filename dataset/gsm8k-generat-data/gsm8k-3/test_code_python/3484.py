def solution():
    """A party hall has 3 decorative light bulbs; a red light bulb which comes on every 2 seconds, a green one every 3 seconds and a blue one every 4 seconds. If they are put on at the same time, what is the shortest time after which the three bulbs will be on at the same time?"""
    # Define the time and status of each light bulb
    red_time, red_status = 2, False
    green_time, green_status = 3, False
    blue_time, blue_status = 4, False

    # Find the time when all three bulbs are on at the same time
    time = 1
    while not (red_status and green_status and blue_status):
        time += 1
        if time % red_time == 0:
            red_status = True
        if time % green_time == 0:
            green_status = True
        if time % blue_time == 0:
            blue_status = True

    # Display the shortest time when all three bulbs are on at the same time
    result = time
    return result

print(solution())