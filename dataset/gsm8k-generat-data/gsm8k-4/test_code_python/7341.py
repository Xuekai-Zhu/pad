def solution():
    """LaKeisha is mowing lawns to raise money for a collector set of books. She charges $.10 for every square foot of lawn. The book set costs $150. If she has already mowed three 20 x 15 foot lawns, how many more square feet does she have to mow to earn enough for the book set?"""
    # Define the cost of the book set and the price per square foot of lawn mowing
    BOOK_SET_COST = 150
    LAWN_PRICE_PER_SQ_FT = 0.1

    # Calculate the total area of the lawns already mowed
    mowed_area = 3 * 20 * 15

    # Calculate the amount of money earned from mowing these lawns
    mowed_money = mowed_area * LAWN_PRICE_PER_SQ_FT

    # Calculate the area that still needs to be mowed to earn the cost of the book set
    remaining_area = (BOOK_SET_COST - mowed_money) / LAWN_PRICE_PER_SQ_FT

    # Display the result
    result = remaining_area
    return result

print(solution())