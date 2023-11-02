def solution():
    """Frank is making hamburgers and he wants to sell them to make $50.  Frank is selling each hamburger for $5 and 2 people purchased 4 and another 2 customers purchased 2 hamburgers.  How many more hamburgers does Frank need to sell to make $50?"""
    # Define the price of one hamburger and the target profit
    hamburger_price = 5
    target_profit = 50

    # Calculate the profit made from the first 2 customers
    profit_customer1 = 4 * hamburger_price
    profit_customer2 = 2 * hamburger_price

    # Calculate the current profit and the number of hamburgers sold
    current_profit = profit_customer1 + profit_customer2
    hamburgers_sold = 6

    # Calculate the remaining profit needed to reach the target
    remaining_profit = target_profit - current_profit

    # Calculate the number of hamburgers needed to make the remaining profit
    hamburgers_needed = remaining_profit / hamburger_price

    # Round up to the nearest integer and return the result
    result = round(hamburgers_needed)
    return result

print(solution())