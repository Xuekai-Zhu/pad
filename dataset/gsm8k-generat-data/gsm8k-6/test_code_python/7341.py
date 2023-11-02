def solution():
    # Calculate the total amount of money LaKeisha earned from mowing 3 lawns
    total_money_earned = 3 * 20 * 15 * 0.10  # LaKeisha charges $.10 for every square foot

    # Calculate the square footage of lawn she still needs to mow to earn enough for the book set
    square_footage_needed = (150 - total_money_earned) / 0.10
    result = square_footage_needed
    return result

print(solution())