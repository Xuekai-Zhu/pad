def solution():
    """Tim decides to start selling necklaces he makes. He uses 10 charms to make each necklace. Each charm cost $15. He sells the necklace for $200. How much profit does he make if he sells 30?"""
    # Define the cost of each charm, the number of charms used per necklace, and the selling price of each necklace
    charm_cost = 15
    charms_per_necklace = 10
    selling_price = 200

    # Calculate the cost of materials for each necklace
    material_cost = charm_cost * charms_per_necklace

    # Calculate the profit per necklace
    profit_per_necklace = selling_price - material_cost

    # Calculate the total profit for selling 30 necklaces
    total_profit = profit_per_necklace * 30

    # Return the result
    result = total_profit
    return result

print(solution())