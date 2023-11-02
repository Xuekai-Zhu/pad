def solution():
    """Theo can eat 13 cookies, 3 times a day, 20 days each month. How many cookies can he eat in 3 months?"""
    # Define the number of cookies Theo can eat in a day
    cookies_per_day = 13 * 3

    # Define the number of days in a month
    days_per_month = 20

    # Calculate the total number of cookies Theo can eat in a month
    cookies_per_month = cookies_per_day * days_per_month

    # Calculate the total number of cookies Theo can eat in 3 months
    cookies_per_three_months = cookies_per_month * 3

    result = cookies_per_three_months
    return result

print(solution())