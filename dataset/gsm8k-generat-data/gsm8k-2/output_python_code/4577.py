def solution():
    """Grace just started her own business. Each week, she charges 300 dollars. Grace's client will pay her every 2 weeks. How many weeks will it take for Grace to get 1800 dollars?"""
    weekly_charge = 300
    total_charge = 1800
    pay_period = 2
    weeks_needed = total_charge // (weekly_charge * pay_period)
    if total_charge % (weekly_charge * pay_period) != 0:
        weeks_needed += 1
    result = weeks_needed
    return result

print(solution())