def solution():
    """Jack is running a bake sale to help pay for his basketball team's uniforms. He's already sold 4 brownies for $3 each and 5 lemon squares for $2 each. If Jack's goal is to make $50 and he sells cookies for $4 each, how many cookies does he need to sell to reach his goal?"""
    # Calculate the total revenue from brownies and lemon squares
    brownie_revenue = 4 * 3
    lemon_square_revenue = 5 * 2
    total_revenue = brownie_revenue + lemon_square_revenue

    # Calculate the amount still needed to reach the goal
    goal = 50
    remaining_goal = goal - total_revenue

    # Calculate the number of cookies to sell to meet the remaining goal
    cookie_price = 4
    cookies_needed = remaining_goal / cookie_price

    # Display the number of cookies needed
    result = cookies_needed
    return result

print(solution())