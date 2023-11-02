def solution():
    """Tim's website got 100 visitors a day for the first 6 days and then on the last day of the week it got twice as many visitors as every other day combined. If he gets $.01 per visit how much did he make that week?"""
    visits_per_day = 100
    days_except_last = 6
    total_visits_except_last = visits_per_day * days_except_last
    last_day_visits = total_visits_except_last * 2
    total_visits = total_visits_except_last + last_day_visits
    earnings_per_visit = 0.01
    total_earnings = total_visits * earnings_per_visit
    result = total_earnings
    return result

print(solution())