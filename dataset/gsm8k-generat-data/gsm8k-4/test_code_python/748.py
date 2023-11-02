def solution():
    """Scarlet saved $80 to spend on jewelry. She bought a pair of earrings that cost $23. Then, she bought a necklace that cost $48. How much of her savings have left?"""
    # Define the initial savings amount
    savings = 80

    # Subtract the cost of the earrings and necklace
    savings -= 23
    savings -= 48

    # Return the remaining savings
    result = savings
    return result

print(solution())