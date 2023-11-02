def solution():
    """Denny is planning to build a modular home.  A 400 square foot Kitchen module costs $20000 and a 150 square foot bathroom module costs $12,000.  All other modules cost $100 per square foot.  If Denny plans to build a 2,000 square foot modular home containing one kitchen and two bathrooms, how much will it cost, in dollars?"""
    # Define the cost of each module
    KITCHEN_COST = 20000
    BATHROOM_COST = 12000
    OTHER_COST_PER_SQ_FT = 100

    # Define the size of each module
    KITCHEN_SIZE = 400
    BATHROOM_SIZE = 150

    # Define the number of each module in the home
    num_kitchens = 1
    num_bathrooms = 2

    # Calculate the cost of the kitchen module
    kitchen_cost = KITCHEN_COST

    # Calculate the cost of the bathroom modules
    bathroom_cost = BATHROOM_COST * num_bathrooms

    # Calculate the cost of the other modules
    other_cost = OTHER_COST_PER_SQ_FT * (2000 - KITCHEN_SIZE - (num_bathrooms * BATHROOM_SIZE))

    # Calculate the total cost of the home
    total_cost = kitchen_cost + bathroom_cost + other_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())