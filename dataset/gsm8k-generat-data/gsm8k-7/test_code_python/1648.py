def solution():
    last_week_total = 324
    this_week_jumps = [34, 20, 0, 123, 64, 23]
    this_week_total = last_week_total
    for jumps in this_week_jumps:
        this_week_total += jumps
    min_jumps_needed = last_week_total + 1 - this_week_total
    result = min_jumps_needed
    return result

print(solution())