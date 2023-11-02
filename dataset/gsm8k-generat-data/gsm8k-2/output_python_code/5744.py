def solution():
    """Barry stands on his head for 10 minutes at a time, but then he must sit for 5 minutes before he can take another turn standing on his head. How many turns can Barry take standing on his head during a single 2-hour period?"""
    total_time = 120  # 2 hours in minutes
    cycle_time = 10 + 5  # time for standing on head plus resting
    num_cycles = total_time // cycle_time  # find number of complete cycles
    remaining_time = total_time % cycle_time  # find remaining time after complete cycles
    num_partial_cycles = 1 if remaining_time >= 10 else 0  # check if enough time for partial cycle
    result = num_cycles + num_partial_cycles
    return result

print(solution())