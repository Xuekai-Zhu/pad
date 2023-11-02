def solution():
    first_lock = 5  # lock 1 stalls raccoons for 5 minutes
    second_lock = 3*(first_lock) - 3  # lock 2 stalls raccoons for 3 minutes less than 3 times as long as lock 1
    both_locks = 5*second_lock  # both locks stall raccoons for 5 times as long as lock 2 alone
    result = both_locks
    return result

print(solution())