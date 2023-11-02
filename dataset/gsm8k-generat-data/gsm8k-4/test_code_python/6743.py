def solution():
    """Jame's buys 100 head of cattle for $40,000. It cost 20% more than that to feed them. They each weigh 1000 pounds and sell for $2 per pound. How much profit did he make?"""
    # Define the initial cost of purchasing the cattle and the cost of feeding them
    INITIAL_COST = 40000
    FEEDING_COST = INITIAL_COST * 0.2

    # Define the weight of each cow and the selling price per pound
    COW_WEIGHT = 1000
    PRICE_PER_POUND = 2

    # Calculate the total weight of all the cows and the total selling price
    total_weight = 100 * COW_WEIGHT
    total_price = total_weight * PRICE_PER_POUND

    # Calculate the total cost of purchasing and feeding the cows
    total_cost = INITIAL_COST + FEEDING_COST

    # Calculate the profit
    profit = total_price - total_cost

    # return the result
    result = profit
    return result

print(solution())