def solution():
    total_ceilings = 28
    ceilings_painted_this_week = 12
    ceilings_painted_next_week = ceilings_painted_this_week / 4
    ceilings_left = total_ceilings - (ceilings_painted_this_week + ceilings_painted_next_week)
    result = ceilings_left
    return result

print(solution())