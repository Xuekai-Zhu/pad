def solution():
    """Josh buys 3 packs of string cheese. Each piece of string cheese costs 10 cents. Each pack has 20 string cheeses in them. How many dollars did he pay?"""
    # Define the number of cheese packs Josh bought and the cost per cheese piece
    NUM_PACKS = 3
    COST_PER_CHEESE = 0.10

    # Calculate the total cost of the cheese
    total_cost = NUM_PACKS * 20 * COST_PER_CHEESE

    # Display the total cost in dollars
    result = total_cost / 100
    return result

print(solution())