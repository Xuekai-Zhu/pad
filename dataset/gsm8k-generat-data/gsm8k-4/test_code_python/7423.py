def solution():
    """A sack of rice, which is 50 kilograms,  costs $50. If David sells it for $1.20 per kilogram, how much will be his profit?"""
    # Define the cost and selling price per kilogram of rice
    cost_per_kilo = 50 / 50  # $1
    selling_price_per_kilo = 1.2

    # Calculate the profit per kilogram
    profit_per_kilo = selling_price_per_kilo - cost_per_kilo

    # Calculate the total profit
    total_profit = profit_per_kilo * 50

    result = total_profit
    return result

print(solution())