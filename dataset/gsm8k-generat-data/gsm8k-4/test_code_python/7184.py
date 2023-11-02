def solution():
    """A vendor at the market is selling sunglasses for $30 each. He has to spend a certain amount to buy these sunglasses. He sells 10 pairs in a day. He then takes half his profits and uses it to buy a new sign, which costs $20. How much does each pair of sunglasses cost him to buy?"""
    # Define the selling price of a pair of sunglasses
    selling_price = 30

    # Define the number of pairs sold in a day
    pairs_sold = 10

    # Calculate the total revenue earned from selling sunglasses in a day
    total_revenue = selling_price * pairs_sold

    # Calculate the cost of the new sign
    sign_cost = 20

    # Calculate the profit earned in a day
    daily_profit = total_revenue - sign_cost

    # Calculate the amount of profit used to buy the new sign
    sign_profit = daily_profit / 2

    # Calculate the remaining profit
    remaining_profit = daily_profit - sign_profit

    # Calculate the cost of each pair of sunglasses
    cost_per_pair = remaining_profit / pairs_sold

    # return the result
    result = cost_per_pair
    return result

print(solution())