def solution():
    """A party hall has 3 decorative light bulbs; a red light bulb which comes on every 2 seconds, a green one every 3 seconds and a blue one every 4 seconds. If they are put on at the same time, what is the shortest time after which the three bulbs will be on at the same time?"""
    red_bulb_time = 2
    green_bulb_time = 3
    blue_bulb_time = 4
    time = 1
    while True:
        if time % red_bulb_time == 0 and time % green_bulb_time == 0 and time % blue_bulb_time == 0:
            result = time
            break
        time += 1
    return result

print(solution())