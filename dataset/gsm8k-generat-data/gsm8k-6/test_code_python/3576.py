def solution():
    # Calculate the total time taken by Billy and Margaret
    billy_time = 2*5 + 4*3 + 1 + billy_final_lap  # time taken by Billy to swim all laps
    margaret_time = 10  # time taken by Margaret to swim all laps

    # Calculate the time taken by Billy to swim his final lap
    billy_final_lap = ((margaret_time + 30) - billy_time)  # Billy finishes 30 seconds before Margaret
    result = billy_final_lap * 60  # convert minutes to seconds
    return result

print(solution())