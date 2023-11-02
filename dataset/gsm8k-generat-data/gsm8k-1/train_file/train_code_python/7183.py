def solution():
    """A vendor at the market is selling sunglasses for $30 each. He has to spend a certain amount to buy these sunglasses. He sells 10 pairs in a day. He then takes half his profits and uses it to buy a new sign, which costs $20. How much does each pair of sunglasses cost him to buy?"""
    sunglasses_price = 30
    sunglasses_sold = 10
    sign_price = 20
    total_profit = sunglasses_sold * sunglasses_price
    half_profit = total_profit / 2
    remaining_profit = half_profit - sign_price
    cost_per_sunglass = remaining_profit / sunglasses_sold
    result = cost_per_sunglass
    return result

print(solution())