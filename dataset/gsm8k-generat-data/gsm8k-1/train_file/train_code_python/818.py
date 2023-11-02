def solution():
    """James decides to build a tin house by collecting 500 tins in a week. On the first day, he collects 50 tins. On the second day, he manages to collect 3 times that number. On the third day, he collects 50 tins fewer than the number he collected on the second day. If he collects an equal number of tins on the remaining days of the week, what's the number of tins he collected each day for the rest of the week?"""
    total_tins = 500
    first_day = 50
    second_day = 3 * first_day
    third_day = second_day - 50
    tins_left = total_tins - first_day - second_day - third_day
    remaining_days = 4
    tins_per_day = tins_left / remaining_days
    result = tins_per_day
    return result

print(solution())