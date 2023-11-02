def solution():
    """Tim decides to start selling necklaces he makes.  He uses 10 charms to make each necklace.  Each charm cost $15.  He sells the necklace for $200.  How much profit does he make if he sells 30?"""
    # Define the cost of each charm
    CHARM_COST = 15

    # Define the number of charms used per necklace
    charms_per_necklace = 10

    # Define the sale price of each necklace
    necklace_price = 200

    # Define the number of necklaces sold
    necklaces_sold = 30

    # Calculate the cost of materials for each necklace
    materials_cost = charms_per_necklace * CHARM_COST

    # Calculate the profit per necklace
    profit_per_necklace = necklace_price - materials_cost

    # Calculate the total profit from selling all necklaces
    total_profit = profit_per_necklace * necklaces_sold

    # Display the total profit
    result = total_profit
    return result

print(solution())