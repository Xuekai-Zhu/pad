def solution():
    """Denny is planning to build a modular home. A 400 square foot Kitchen module costs $20000 and a 150 square foot bathroom module costs $12,000. All other modules cost $100 per square foot. If Denny plans to build a 2,000 square foot modular home containing one kitchen and two bathrooms, how much will it cost, in dollars?"""
    square_footage = 2000
    kitchen_cost = 20000
    bathroom_cost = 12000
    other_modules_cost = (square_footage - 400 - 2 * 150) * 100
    total_cost = kitchen_cost + 2 * bathroom_cost + other_modules_cost
    result = total_cost
    return result

print(solution())