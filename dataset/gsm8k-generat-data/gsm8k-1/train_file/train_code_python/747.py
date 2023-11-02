def solution():
    """Scarlet saved $80 to spend on jewelry. She bought a pair of earrings that cost $23. Then, she bought a necklace that cost $48. How much of her savings have left?"""
    starting_savings = 80
    earrings_cost = 23
    necklace_cost = 48
    total_spent = earrings_cost + necklace_cost
    savings_left = starting_savings - total_spent
    result = savings_left
    return result

print(solution())