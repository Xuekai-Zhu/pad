def solution():
    """James decides to build a tin house by collecting 500 tins in a week. On the first day, he collects 50 tins. On the second day, he manages to collect 3 times that number. On the third day, he collects 50 tins fewer than the number he collected on the second day. If he collects an equal number of tins on the remaining days of the week, what's the number of tins he collected each day for the rest of the week?"""
    total_tins = 500
    day_one_tins = 50
    day_two_tins = 3 * day_one_tins
    day_three_tins = day_two_tins - 50
    tins_left = total_tins - day_one_tins - day_two_tins - day_three_tins
    remaining_days = 4
    tins_per_day = tins_left / remaining_days
    result = tins_per_day
    return result

print(solution())