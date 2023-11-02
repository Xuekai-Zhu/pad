def solution():
    brownies_sold = 4
    brownies_price = 3

    lemon_squares_sold = 5
    lemon_squares_price = 2

    target_goal = 50

    cookie_price = 4

    # Calculate the total amount of money already earned from brownies and lemon squares
    total_earned = (brownies_sold * brownies_price) + (lemon_squares_sold * lemon_squares_price)

    # Calculate the amount of money needed to reach the goal
    remaining_goal = target_goal - total_earned

    # Calculate the number of cookies needed to reach the remaining goal
    num_cookies_needed = remaining_goal / cookie_price
    result = num_cookies_needed
    return result

print(solution())