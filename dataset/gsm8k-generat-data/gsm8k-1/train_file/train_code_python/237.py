def solution():
    """Jack is running a bake sale to help pay for his basketball team's uniforms. He's already sold 4 brownies for $3 each and 5 lemon squares for $2 each. If Jack's goal is to make $50 and he sells cookies for $4 each, how many cookies does he need to sell to reach his goal?"""
    brownies_sold = 4
    brownie_price = 3
    total_brownie_sales = brownies_sold * brownie_price
    
    lemon_squares_sold = 5
    lemon_square_price = 2
    total_lemon_square_sales = lemon_squares_sold * lemon_square_price
    
    current_sales = total_brownie_sales + total_lemon_square_sales
    goal_sales = 50
    
    cookies_price = 4
    cookies_needed = (goal_sales - current_sales) / cookies_price
    result = cookies_needed
    
    return result

print(solution())