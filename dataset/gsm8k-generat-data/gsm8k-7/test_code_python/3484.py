def solution():
    red_time = 2
    green_time = 3
    blue_time = 4

    time = 1

    # Loop until all three bulbs are on at the same time
    while True:
        if time % red_time == 0 and time % green_time == 0 and time % blue_time == 0:
            result = time
            break

        time += 1

    return result

print(solution())