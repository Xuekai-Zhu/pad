def solution():
    """A king gets a crown made that costs $20,000. He tips the person 10%. How much did the king pay after the tip?"""
    crown_cost = 20000
    tip_percent = 0.1
    tip_amount = crown_cost * tip_percent
    total_cost = crown_cost + tip_amount
    result = total_cost
    return result

print(solution())