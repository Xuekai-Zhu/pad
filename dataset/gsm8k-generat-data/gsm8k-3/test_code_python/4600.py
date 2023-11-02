def solution():
    """Nick is trying to raise money for a charity. He is selling candy bars for $5. He is also selling chocolate oranges for $10. He wants to raise $1000. He only had 20 chocolate oranges that he sold out. How many candy bars does Nick need to sell to reach his goal?"""
    # Define the prices of the candy bars and chocolate oranges
    CANDY_PRICE = 5
    ORANGE_PRICE = 10

    # Define the number of chocolate oranges sold
    oranges_sold = 20

    # Define the desired amount to raise
    desired_amount = 1000

    # Calculate the amount raised from the chocolate oranges
    orange_sales = oranges_sold * ORANGE_PRICE

    # Calculate the amount still needed to reach the desired amount
    remaining_amount = desired_amount - orange_sales

    # Calculate the number of candy bars needed to reach the remaining amount
    candy_needed = remaining_amount / CANDY_PRICE

    # Round up to the nearest integer, since Nick can't sell a partial candy bar
    candy_needed = int(candy_needed + 0.5)

    # Display the number of candy bars needed
    result = candy_needed
    return result

print(solution())