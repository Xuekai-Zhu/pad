def solution():
    """John buys 30 ducks for $10 each. They weigh 4 pounds and he sells them for $5 per pound. How much profit did he make?"""
    # Define the cost per duck and the number of ducks purchased
    COST_PER_DUCK = 10
    NUM_DUCKS = 30

    # Calculate the total cost of the ducks
    total_cost = COST_PER_DUCK * NUM_DUCKS

    # Calculate the total weight of the ducks
    total_weight = NUM_DUCKS * 4

    # Calculate the total revenue from selling the ducks
    total_revenue = total_weight * 5

    # Calculate the profit by subtracting the total cost from the total revenue
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())