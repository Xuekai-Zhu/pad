def solution():
    """A jewelry box has 10 necklaces and 15 earrings. Jessy goes to the jewelry stores and buys 10 more necklaces and 2/3 as many earrings as before. After returning home, her mother gives her 1/5 times more earrings than the number she purchased at the store. Calculate the total number of jewelry pieces Jessy has in her box if she puts all of them together."""
    # Define the initial number of necklaces and earrings
    initial_necklaces = 10
    initial_earrings = 15

    # Calculate the new number of necklaces after Jessy goes to the store
    new_necklaces = initial_necklaces + 10

    # Calculate the new number of earrings after Jessy goes to the store
    new_earrings = int(round(initial_earrings * (2/3))) + int(round((2/5) * (initial_earrings * (2/3))))

    # Calculate the total number of jewelry pieces
    total_jewelry = new_necklaces + new_earrings

    # return the result
    result = total_jewelry
    return result

print(solution())