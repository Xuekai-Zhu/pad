def solution():
    """A farmer is growing corn. For every 4 seeds he plants, he gets one ear of corn, that he can sell for $.1. It costs $.5 for a bag with 100 seeds. If he makes $40 in profit, how many ears did he sell?"""
    # Define the cost and revenue per ear of corn
    COST_PER_SEED = 0.005
    REVENUE_PER_EAR = 0.1

    # Calculate the profit per ear of corn
    PROFIT_PER_EAR = REVENUE_PER_EAR - COST_PER_SEED * 4

    # Calculate the number of ears of corn needed to make a profit of $40
    ears_needed = int(40 / PROFIT_PER_EAR)

    # Calculate the number of seeds needed to grow the required number of ears
    seeds_needed = ears_needed * 4

    # Calculate the cost of the required number of seeds
    seed_cost = seeds_needed * COST_PER_SEED

    # Calculate the revenue from selling the required number of ears
    revenue = ears_needed * REVENUE_PER_EAR

    # Calculate the profit
    profit = revenue - seed_cost - 40

    # Display the number of ears sold
    result = ears_needed
    return result

print(solution())