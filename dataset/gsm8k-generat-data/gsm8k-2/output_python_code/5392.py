def solution():
    """Denny is planning to build a modular home. A 400 square foot Kitchen module costs $20000 and a 150 square foot bathroom module costs $12,000. All other modules cost $100 per square foot. If Denny plans to build a 2,000 square foot modular home containing one kitchen and two bathrooms, how much will it cost, in dollars?"""
    kitchen_cost = 20000
    bathroom_cost = 12000
    other_cost = 100
    total_area = 2000
    kitchen_area = 400
    bathroom_area = 150
    other_area = total_area - kitchen_area - (2 * bathroom_area)
    total_cost = (kitchen_cost + (2 * bathroom_cost) + (other_area * other_cost))
    result = total_cost
    return result

print(solution())