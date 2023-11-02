def solution():
    """Françoise sells pots of lily of the valley to fund humanitarian work. She buys them at €12 each and sells them at a 25% higher cost. How much will she give back to the association by selling 150 pots of lily of the valley?"""
    # Define the cost and selling price of each pot
    cost_per_pot = 12
    selling_price_per_pot = cost_per_pot * 1.25

    # Calculate the profit per pot
    profit_per_pot = selling_price_per_pot - cost_per_pot

    # Calculate the total profit from selling 150 pots
    total_profit = profit_per_pot * 150

    # Return the amount to be given back to the association
    result = total_profit
    return result

print(solution())