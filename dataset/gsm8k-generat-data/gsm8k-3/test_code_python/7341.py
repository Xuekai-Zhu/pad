def solution():
    """LaKeisha is mowing lawns to raise money for a collector set of books. She charges $.10 for every square foot of lawn. The book set costs $150. If she has already mowed three 20 x 15 foot lawns, how many more square feet does she have to mow to earn enough for the book set?"""
    # Define the cost per square foot and the cost of the book set
    COST_PER_SQ_FT = 0.10
    BOOK_SET_COST = 150

    # Calculate the total area of the lawns already mowed
    mowed_area = 3 * 20 * 15

    # Calculate the amount of money earned from the lawns already mowed
    mowed_earnings = mowed_area * COST_PER_SQ_FT

    # Calculate the amount of money still needed to purchase the book set
    remaining_cost = BOOK_SET_COST - mowed_earnings

    # Calculate the amount of square footage needed to earn the remaining money
    remaining_area = remaining_cost / COST_PER_SQ_FT

    result = remaining_area
    return result

print(solution())