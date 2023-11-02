def solution():
    total_ceilings = 28
    this_week_ceiling = 12
    next_week_ceiling = this_week_ceiling / 4

    # Calculate the total number of ceilings left to paint after next week
    remaining_ceilings = total_ceilings - (this_week_ceiling + next_week_ceiling)
    result = remaining_ceilings
    return result

print(solution())