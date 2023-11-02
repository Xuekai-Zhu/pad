def solution():
    """Josh buys 3 packs of string cheese. Each piece of string cheese costs 10 cents. Each pack has 20 string cheeses in them. How many dollars did he pay?"""
    # Define the cost and quantity of string cheese
    CHEESE_COST = 0.1 # 10 cents
    CHEESE_QUANTITY = 3 * 20 # 3 packs with 20 cheeses each

    # Calculate the total cost of the string cheese
    total_cost = CHEESE_COST * CHEESE_QUANTITY

    # return the result in dollars
    result = total_cost / 100
    return result

print(solution())