def solution():
    candy_bar_price = 5
    chocolate_orange_price = 10
    total_goal = 1000
    num_chocolate_oranges = 20

    # Calculate the total amount raised from selling chocolate oranges
    total_chocolate_orange_sale = num_chocolate_oranges * chocolate_orange_price

    # Calculate the remaining amount needed to reach the goal
    remaining_goal = total_goal - total_chocolate_orange_sale

    # Calculate the number of candy bars needed to reach the remaining goal
    num_candy_bars_needed = remaining_goal / candy_bar_price
    result = num_candy_bars_needed
    return result

print(solution())