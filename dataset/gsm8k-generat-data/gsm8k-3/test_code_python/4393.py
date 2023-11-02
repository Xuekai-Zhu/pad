def solution():
    """Hallie is an artist. She wins an art contest, and she receives a $150 prize. She sells 3 of her paintings for $50 each. How much money does she make in total from her art?"""
    # Define the prize and the price per painting
    PRIZE = 150
    PRICE_PER_PAINTING = 50

    # Calculate the total amount of money made from selling paintings
    painting_income = 3 * PRICE_PER_PAINTING

    # Calculate the total amount of money made
    total_income = PRIZE + painting_income

    # Display the total income
    result = total_income
    return result

print(solution())