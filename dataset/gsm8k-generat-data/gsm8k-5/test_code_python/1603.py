def solution():
    cookies_per_day = 13 * 3  # Theo can eat 13 cookies, 3 times a day
    days_per_month = 20  # Theo can eat cookies for 20 days each month
    months = 3  # Theo wants to know how many cookies he can eat in 3 months

    # Calculate the total number of cookies Theo can eat in 3 months
    total_cookies = cookies_per_day * days_per_month * months
    result = total_cookies
    return result

print(solution())