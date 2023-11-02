def solution():
    # Calculate the number of racers at the start of the race
    start_racers = 50  

    # Calculate the number of racers after 20 minutes
    after_20_min = start_racers + 30  

    # Calculate the number of racers after another 30 minutes
    after_another_30 = after_20_min * 2  

    # Calculate the number of racers who dropped out of the race
    dropped_out = after_another_30 - 130  

    result = dropped_out
    return result

print(solution())