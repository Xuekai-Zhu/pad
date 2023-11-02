def solution():
    """Barry stands on his head for 10 minutes at a time, but then he must sit for 5 minutes before he can take another turn standing on his head. How many turns can Barry take standing on his head during a single 2-hour period?"""
    standing_time = 10
    sitting_time = 5
    total_time = 120
    time_per_round = standing_time + sitting_time
    rounds_per_hour = 60 / time_per_round
    total_rounds = rounds_per_hour * 2
    result = int(total_rounds)
    return result

print(solution())