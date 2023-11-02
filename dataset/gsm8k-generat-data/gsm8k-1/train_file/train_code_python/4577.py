def solution():
    """Grace just started her own business. Each week, she charges 300 dollars. Grace's client will pay her every 2 weeks. How many weeks will it take for Grace to get 1800 dollars?"""
    weekly_rate = 300
    payment_period = 2
    total_payment = 1800
    weeks = total_payment / (weekly_rate * payment_period)
    result = weeks
    return result

print(solution())