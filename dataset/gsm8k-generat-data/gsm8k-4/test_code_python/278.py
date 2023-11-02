def solution():
    """The price of a home is $98 per square foot (sq ft). The house is 2,400 sq ft and the barn out back is 1,000 sq ft. How much is this property?"""
    # Define the price per square foot and the sizes of the house and barn
    PRICE_PER_SQ_FT = 98
    HOUSE_SIZE = 2400
    BARN_SIZE = 1000

    # Calculate the total size of the property
    total_size = HOUSE_SIZE + BARN_SIZE

    # Calculate the total price of the property
    total_price = total_size * PRICE_PER_SQ_FT

    result = total_price
    return result

print(solution())