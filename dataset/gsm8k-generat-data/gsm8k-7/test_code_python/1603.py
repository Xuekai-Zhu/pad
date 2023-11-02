def solution():
    cookies_per_day = 13
    num_meals_per_day = 3
    num_days_per_month = 20
    num_months = 3

    # Calculate the total number of cookies Theo can eat each day
    total_cookies_per_day = cookies_per_day * num_meals_per_day

    # Calculate the total number of cookies Theo can eat in one month
    total_cookies_per_month = total_cookies_per_day * num_days_per_month

    # Calculate the total number of cookies Theo can eat in three months
    total_cookies = total_cookies_per_month * num_months
    result = total_cookies
    return result

print(solution())