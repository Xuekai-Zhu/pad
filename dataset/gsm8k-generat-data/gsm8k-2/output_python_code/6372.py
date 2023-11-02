def solution():
    """Tim's website got 100 visitors a day for the first 6 days and then on the last day of the week it got twice as many visitors as every other day combined. If he gets $.01 per visit how much did he make that week?"""
    first_six_days = 100 * 6
    last_day = 2 * (100 * 6)

    total_visitors = first_six_days + last_day
    earnings = total_visitors * 0.01
    result = earnings
    return result

print(solution())