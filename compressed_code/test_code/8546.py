def solution():
    
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