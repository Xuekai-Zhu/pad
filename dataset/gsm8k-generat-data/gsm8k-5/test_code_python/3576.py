def solution():
    # Calculate total time taken by Billy to swim 9 laps
    total_time = 2*5 + 4*3 + 1*1  # 2 min per 5 laps, 4 min per 3 laps, 1 min per 1 lap

    # Calculate time taken by Billy to swim 10 laps
    # Billy finished 30 seconds before Margaret, so he took 30 seconds less than her
    time_10_laps = (10*60 - total_time - 30)

    # Calculate time taken by Billy to swim his final lap
    time_final_lap = time_10_laps - (2*5 + 4*3 + 1)

    result = time_final_lap
    return result

print(solution())