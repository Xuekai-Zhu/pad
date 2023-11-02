def solution():
    
    current_sales = (4 * 3) + (5 * 2)
    goal_sales = 50
    remaining_sales = goal_sales - current_sales
    cookie_price = 4
    cookies_needed = remaining_sales / cookie_price
    result = cookies_needed
    return result

print(solution())