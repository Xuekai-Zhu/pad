def solution():
    """Theo can eat 13 cookies, 3 times a day, 20 days each month. How many cookies can he eat in 3 months?"""
    cookies_per_day = 13 * 3
    days_per_month = 20
    cookies_per_month = cookies_per_day * days_per_month
    cookies_in_3_months = cookies_per_month * 3
    result = cookies_in_3_months
    return result

print(solution())