def solution():
    """Theo can eat 13 cookies, 3 times a day, 20 days each month. How many cookies can he eat in 3 months?"""
    # Define the number of cookies Theo can eat per day
    cookies_per_day = 13 * 3

    # Define the number of days Theo eats cookies each month
    days_per_month = 20

    # Calculate the number of cookies Theo can eat in a month
    cookies_per_month = cookies_per_day * days_per_month

    # Calculate the number of cookies Theo can eat in 3 months
    cookies_per_3_months = cookies_per_month * 3

    # Display the total number of cookies Theo can eat in 3 months
    result = cookies_per_3_months
    return result

print(solution())