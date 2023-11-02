def solution():
    """A vendor at the market is selling sunglasses for $30 each. He has to spend a certain amount to buy these sunglasses. He sells 10 pairs in a day. He then takes half his profits and uses it to buy a new sign, which costs $20. How much does each pair of sunglasses cost him to buy?"""
    selling_price = 30
    total_pairs_sold = 10
    total_sales = selling_price * total_pairs_sold
    sign_cost = 20
    profit = total_sales - sign_cost
    cost_per_pair = profit / total_pairs_sold
    result = cost_per_pair
    return result

print(solution())