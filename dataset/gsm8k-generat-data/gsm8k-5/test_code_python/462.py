def solution():
    roberto_speed = 4200  # Roberto can skip 4,200 times an hour
    valerie_speed = 80 * 15  # Valerie can skip 80 times a minute for 15 minutes

    # Calculate the total number of skips
    total_skips = roberto_speed + valerie_speed
    result = total_skips
    return result

print(solution())