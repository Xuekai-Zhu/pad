def solution():
    # Calculate the total spent on non-cookie items
    non_cookie_total = 3 + (2 * 3.5) + (4 * 0.25) + (4 * 0.5)

    # Calculate the remaining budget for cookies
    cookie_budget = 25 - non_cookie_total

    # Calculate the cost of one box of cookies
    milk_cost = 3
    cookie_cost_ratio = 2
    cookie_cost = milk_cost * cookie_cost_ratio

    # Calculate the number of boxes of cookies Steve can buy
    num_cookies = cookie_budget / cookie_cost
    result = num_cookies
    return result

print(solution())