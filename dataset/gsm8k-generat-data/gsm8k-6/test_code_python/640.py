def solution():
    # Calculate the number of ceilings left to paint after next week
    total_ceiling = 28
    painted_this_week = 12
    painted_next_week = 1/4 * painted_this_week
    ceilings_left = total_ceiling - painted_this_week - painted_next_week
    result = ceilings_left
    return result

print(solution())