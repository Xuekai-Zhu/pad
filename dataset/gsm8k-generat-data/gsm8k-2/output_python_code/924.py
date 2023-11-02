def solution():
    """Ann, Becky, and Julia are working at a pharmacy, every day for 8 hours. Each of them is providing service to 7 customers per hour. One day Julia had to finish her work earlier, so she was working only for 6 hours. How many customers did all three of these women serve that day in total?"""
    hours_per_day = 8
    customers_per_hour = 7
    total_customers = (hours_per_day * customers_per_hour) * 3
    julia_customers = (customers_per_hour * 6)
    total_customers -= julia_customers
    result = total_customers
    return result

print(solution())