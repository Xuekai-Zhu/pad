def solution():
    """James decides to build a tin house by collecting 500 tins in a week. On the first day, he collects 50 tins. On the second day, he manages to collect 3 times that number. On the third day, he collects 50 tins fewer than the number he collected on the second day. If he collects an equal number of tins on the remaining days of the week, what's the number of tins he collected each day for the rest of the week?"""
    # Define the number of tins collected on each day
    day_1 = 50
    day_2 = day_1 * 3
    day_3 = day_2 - 50
    remaining_tins = 500 - day_1 - day_2 - day_3
    remaining_days = 4
    daily_tins = remaining_tins / remaining_days

    # return the result
    result = daily_tins
    return result

print(solution())