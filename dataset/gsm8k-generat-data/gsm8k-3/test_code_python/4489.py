def solution():
    """Michael has $50. He wants to surprise his mom on Mother's day by buying a cake for $20, a bouquet for $36, and a set of balloons for $5. How much more money does Michael need to buy all those?"""
    # Define the cost of the cake, bouquet, and balloons
    CAKE_COST = 20
    BOUQUET_COST = 36
    BALLOONS_COST = 5

    # Define Michael's starting budget
    BUDGET = 50

    # Calculate the total cost of the items Michael wants to buy
    total_cost = CAKE_COST + BOUQUET_COST + BALLOONS_COST

    # Calculate how much more money Michael needs to buy everything
    remaining_budget = total_cost - BUDGET

    # Display how much more money Michael needs to buy everything
    result = remaining_budget
    return result

print(solution())