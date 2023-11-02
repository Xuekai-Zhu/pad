def solution():
    # Define the prices and quantities of candy bars and chocolate oranges
    candy_bar_price = 5
    candy_bar_quantity = x
    chocolate_orange_price = 10
    chocolate_orange_quantity = 20

    # Calculate the total amount of money raised
    total_money_raised = (candy_bar_price * candy_bar_quantity) + (chocolate_orange_price * chocolate_orange_quantity)

    # Calculate the number of candy bars needed to reach the goal
    candy_bars_needed = (1000 - total_money_raised) / candy_bar_price
    result = candy_bars_needed
    return result

print(solution())