def solution():
    # Calculate the total number of jumps Spencer will do in 5 days
    jumps_per_session = 4 * 10  # Spencer jumps 4 times per minute for 10 minutes
    jumps_per_day = jumps_per_session * 2  # Spencer does 2 sessions each day
    total_jumps = jumps_per_day * 5  # Spencer does this for 5 days
    result = total_jumps
    return result

print(solution())