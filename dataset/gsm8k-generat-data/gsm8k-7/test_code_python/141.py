def solution():
    playtime_per_day = 0.5 + 0.5  # 30 minutes twice a day = 1 hour total
    feeding_time_per_day = 0.2  # 1/5 of an hour

    # Convert playtime and feeding time to minutes
    total_playtime = playtime_per_day * 60  # 60 minutes in an hour
    total_feeding_time = feeding_time_per_day * 60

    # Calculate the total time Larry spends on his dog each day
    total_time = total_playtime + total_feeding_time
    result = total_time
    return result

print(solution())