def solution():
    """Casey is going to stay at a motel while she works her summer job as a ski instructor. The hotel charges $280/week or $1000/month. If Casey will be staying 3 months, each with exactly 4 weeks, how much money does she save by paying monthly?"""
    weekly_cost = 280
    monthly_cost = 1000
    weeks_in_month = 4
    months_staying = 3
    total_weekly_cost = weekly_cost * weeks_in_month * months_staying
    total_monthly_cost = monthly_cost * months_staying
    savings = total_weekly_cost - total_monthly_cost
    result = savings
    return result

print(solution())