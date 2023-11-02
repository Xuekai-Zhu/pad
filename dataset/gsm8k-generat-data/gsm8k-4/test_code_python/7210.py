def solution():
    """Peter is eating chips. Each chip is 10 calories. A bag has 24 chips and costs $2. If he wants to eat 480 calories, how much does he have to spend on chips?"""
    # Define the number of calories per chip and the number of chips per bag
    CALORIES_PER_CHIP = 10
    CHIPS_PER_BAG = 24

    # Calculate the number of bags needed to eat 480 calories
    bags_needed = 480 / CALORIES_PER_CHIP / CHIPS_PER_BAG

    # Calculate the cost of the required number of bags
    total_cost = bags_needed * 2

    # round and return the result
    result = round(total_cost, 2)
    return result

print(solution())