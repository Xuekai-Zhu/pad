def solution():
    """Scarlet saved $80 to spend on jewelry. She bought a pair of earrings that cost $23. Then, she bought a necklace that cost $48. How much of her savings have left?"""
    total_savings = 80
    earrings_cost = 23
    necklace_cost = 48
    total_spent = earrings_cost + necklace_cost
    remaining_savings = total_savings - total_spent
    result = remaining_savings
    return result

print(solution())