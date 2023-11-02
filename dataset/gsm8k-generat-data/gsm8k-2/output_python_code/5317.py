def solution():
    """Casey is going to stay at a motel while she works her summer job as a ski instructor. The hotel charges $280/week or $1000/month. If Casey will be staying 3 months, each with exactly 4 weeks, how much money does she save by paying monthly?"""
    weekly_rate = 280
    monthly_rate = 1000
    num_weeks_per_month = 4
    num_months = 3
    total_weekly_cost = weekly_rate * num_weeks_per_month * num_months
    total_monthly_cost = monthly_rate * num_months
    amount_saved = total_weekly_cost - total_monthly_cost
    result = amount_saved
    return result

print(solution())