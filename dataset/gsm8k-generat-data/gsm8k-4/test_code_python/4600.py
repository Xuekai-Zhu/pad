def solution():
    """Nick is trying to raise money for a charity. He is selling candy bars for $5. He is also selling chocolate oranges for $10. He wants to raise $1000. He only had 20 chocolate oranges that he sold out. How many candy bars does Nick need to sell to reach his goal?"""
    # Define the prices of candy bars and chocolate oranges
    candy_bar_price = 5
    chocolate_orange_price = 10

    # Define the number of chocolate oranges sold
    chocolate_oranges_sold = 20

    # Calculate the amount of money raised from chocolate oranges
    chocolate_oranges_money = chocolate_orange_price * chocolate_oranges_sold

    # Calculate the amount of money raised from candy bars needed to reach the goal
    remaining_money = 1000 - chocolate_oranges_money
    candy_bars_needed = remaining_money / candy_bar_price

    # Round up to the nearest whole number
    candy_bars_needed = int(candy_bars_needed) + 1

    # return the result
    result = candy_bars_needed
    return result

print(solution())