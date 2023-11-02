def solution():
    """Jack is running a bake sale to help pay for his basketball team's uniforms. He's already sold 4 brownies for $3 each and 5 lemon squares for $2 each. If Jack's goal is to make $50 and he sells cookies for $4 each, how many cookies does he need to sell to reach his goal?"""
    # Define the total amount earned from selling brownies and lemon squares
    total_earned = (4 * 3) + (5 * 2)

    # Define the amount still needed to reach the goal
    amount_needed = 50 - total_earned

    # Calculate the number of cookies needed to reach the goal
    cookies_needed = amount_needed / 4

    # Round up to the nearest whole number
    cookies_needed = math.ceil(cookies_needed)

    result = cookies_needed
    return result

print(solution())