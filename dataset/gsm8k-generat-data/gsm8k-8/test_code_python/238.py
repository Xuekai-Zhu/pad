def solution():
    # Calculate the total amount made from the brownies and lemon squares
    total_brownies = 4 * 3
    total_lemon_squares = 5 * 2
    total_sale = total_brownies + total_lemon_squares

    # Calculate how much more money is needed to reach the goal
    money_left = 50 - total_sale

    # Calculate how many cookies need to be sold
    cookies_needed = money_left / 4

    result = cookies_needed
    return result

print(solution())