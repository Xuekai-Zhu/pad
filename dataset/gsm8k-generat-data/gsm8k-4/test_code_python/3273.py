def solution():
    """A farmer is growing corn. For every 4 seeds he plants, he gets one ear of corn, that he can sell for $.1. It costs $.5 for a bag with 100 seeds. If he makes $40 in profit, how many ears did he sell?"""
    # Define the cost of seeds, the selling price per ear, and the profit goal
    seed_cost = 0.5
    ear_price = 0.1
    profit_goal = 40

    # Calculate the number of ears that can be produced from 100 seeds
    ears_per_bag = 100 // 4

    # Calculate the cost per ear based on the seed cost
    cost_per_ear = seed_cost / ears_per_bag

    # Calculate the profit per ear
    profit_per_ear = ear_price - cost_per_ear

    # Calculate the number of ears needed to reach the profit goal
    ears_needed = profit_goal / profit_per_ear

    # Round up to the nearest integer, since ears cannot be sold in fractional amounts
    ears_sold = int(ears_needed + 0.5)

    result = ears_sold
    return result

print(solution())