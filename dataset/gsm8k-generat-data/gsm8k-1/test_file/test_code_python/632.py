def solution():
    """Julie operates the cash register exactly twice as fast as her less-experienced colleague Jewel.
    Daily, Jewel processes 50 customers. What is the total weekly production for the two if they work all days of the week?"""
    jewel_daily = 50
    julie_daily = jewel_daily * 2
    days_per_week = 7
    total_customers = (jewel_daily + julie_daily) * days_per_week
    result = total_customers
    return result

print(solution())