def solution():
    """A jewelry box has 10 necklaces and 15 earrings. Jessy goes to the jewelry stores and buys 10 more necklaces and 2/3 as many earrings as before. After returning home, her mother gives her 1/5 times more earrings than the number she purchased at the store. Calculate the total number of jewelry pieces Jessy has in her box if she puts all of them together."""
    # Define the initial number of necklaces and earrings in the jewelry box
    initial_necklaces = 10
    initial_earrings = 15

    # Calculate the total number of necklaces and earrings Jessy has after going to the store
    new_necklaces = initial_necklaces + 10
    new_earrings = (2/3) * initial_earrings
    total_pieces = new_necklaces + new_earrings

    # Calculate the number of earrings Jessy's mother gives her
    additional_earrings = (1/5) * new_earrings

    # Calculate the final total number of jewelry pieces Jessy has
    final_total = total_pieces + additional_earrings

    # Display the final total number of jewelry pieces
    result = final_total
    return result

print(solution())