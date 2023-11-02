def solution():
    # Define the number of cookies sold and the total earnings
    num_cookies_sold = 50
    total_earnings = 60

    # Calculate the average earnings per cookie
    earnings_per_cookie = total_earnings / num_cookies_sold

    # Calculate the cost of making each cookie
    cost_per_cookie = earnings_per_cookie / 1.2

    result = cost_per_cookie
    return result

print(solution())