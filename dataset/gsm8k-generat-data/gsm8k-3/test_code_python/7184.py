def solution():
    """A vendor at the market is selling sunglasses for $30 each. He has to spend a certain amount to buy these sunglasses. He sells 10 pairs in a day. He then takes half his profits and uses it to buy a new sign, which costs $20. How much does each pair of sunglasses cost him to buy?"""
    # Define the selling price of each pair of sunglasses
    SELLING_PRICE = 30

    # Define the number of pairs of sunglasses sold in a day
    PAIRS_SOLD = 10

    # Calculate the total revenue for a day
    total_revenue = SELLING_PRICE * PAIRS_SOLD

    # Calculate the cost of the new sign
    sign_cost = 20

    # Calculate the profit for a day
    profit = total_revenue - sign_cost

    # Calculate the amount spent on buying the sunglasses
    sunglasses_cost = profit / 2

    # Calculate the cost of each pair of sunglasses
    cost_per_pair = sunglasses_cost / PAIRS_SOLD

    # Display the cost per pair of sunglasses
    result = cost_per_pair
    return result

print(solution())