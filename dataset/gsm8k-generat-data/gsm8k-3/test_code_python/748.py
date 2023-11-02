def solution():
    """Scarlet saved $80 to spend on jewelry. She bought a pair of earrings that cost $23. Then, she bought a necklace that cost $48. How much of her savings have left?"""
    # Define the initial savings and the cost of each jewelry piece 
    savings = 80
    earrings_cost = 23
    necklace_cost = 48

    # Calculate the total cost of the jewelry pieces
    total_cost = earrings_cost + necklace_cost

    # Calculate the amount of money left from the original savings
    remaining_savings = savings - total_cost

    # Display the amount of money left
    result = remaining_savings
    return result

print(solution())