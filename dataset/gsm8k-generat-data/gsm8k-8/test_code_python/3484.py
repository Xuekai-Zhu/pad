def solution():
    # Initialize time counter and flag variables
    time = 0
    red_flag = False
    green_flag = False
    blue_flag = False

    # Loop until all bulbs are on at the same time
    while not (red_flag and green_flag and blue_flag):
        time += 1  # Increment time counter

        # Check if red bulb should be on
        if time % 2 == 0:
            red_flag = True

        # Check if green bulb should be on
        if time % 3 == 0:
            green_flag = True

        # Check if blue bulb should be on
        if time % 4 == 0:
            blue_flag = True

    result = time
    return result

print(solution())