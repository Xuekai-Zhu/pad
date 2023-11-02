def solution():
    """Denny is planning to build a modular home.  A 400 square foot Kitchen module costs $20000 and a 150 square foot bathroom module costs $12,000.  All other modules cost $100 per square foot.  If Denny plans to build a 2,000 square foot modular home containing one kitchen and two bathrooms, how much will it cost, in dollars?"""
    # Calculate the cost of the kitchen module
    kitchen_cost = 20000

    # Calculate the cost of two bathroom modules
    bathroom_cost = 2 * 12000

    # Calculate the cost of other modules
    other_cost = (2000 - 400 - 300) * 100

    # Calculate the total cost of the modular home
    total_cost = kitchen_cost + bathroom_cost + other_cost

    # return the result
    result = total_cost
    return result

print(solution())