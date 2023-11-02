def solution():
    """Ursula went to the store and bought butter, bread, a package of cheese, and tea. The bread was 2 times cheaper than the butter, while the price of the butter was 80% of the price of cheese. Tea was the most expensive and cost twice the price of a package of cheese. If the tea cost $10, how much did Ursula pay for her purchases?"""
    # Define the price of tea and the tea-to-cheese price ratio
    tea_price = 10
    cheese_price_ratio = 0.5

    # Calculate the price of cheese
    cheese_price = tea_price * cheese_price_ratio

    # Calculate the price of butter
    butter_price = cheese_price * 0.8

    # Calculate the price of bread
    bread_price = butter_price / 2

    # Calculate the total cost of Ursula's purchases
    total_cost = tea_price + cheese_price + butter_price + bread_price

    result = total_cost
    return result

print(solution())