def solution():
    """Jack is running a bake sale to help pay for his basketball team's uniforms. He's already sold 4 brownies for $3 each and 5 lemon squares for $2 each. If Jack's goal is to make $50 and he sells cookies for $4 each, how many cookies does he need to sell to reach his goal?"""
    current_sales = (4 * 3) + (5 * 2)
    goal_sales = 50
    remaining_sales = goal_sales - current_sales
    cookie_price = 4
    cookies_needed = remaining_sales / cookie_price
    result = cookies_needed
    return result

print(solution())