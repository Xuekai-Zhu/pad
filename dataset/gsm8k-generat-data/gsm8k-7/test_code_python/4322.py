def solution():
    distance = 1200
    speed1 = 50
    speed2 = 60

    # Calculate the time it takes to travel the distance at speed 1
    time1 = distance / speed1

    # Calculate the time it takes to travel the distance at speed 2
    time2 = distance / speed2

    # Calculate the time saved by driving at a faster speed
    time_saved = time1 - time2
    result = time_saved
    return result

print(solution())