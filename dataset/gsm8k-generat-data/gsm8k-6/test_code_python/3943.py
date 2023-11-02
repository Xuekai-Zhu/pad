def solution():
    # Calculate the number of necklaces and earrings Jessy has after buying more
    new_necklaces = 10 + 10  # Jessy buys 10 more necklaces
    old_earrings = 15
    new_earrings = 2/3 * old_earrings  # Jessy buys 2/3 as many earrings as before
    total_earrings = new_earrings + (1/5 * new_earrings)  # Jessy's mother gives her 1/5 more earrings than the ones she purchased
    total_jewelry = new_necklaces + total_earrings  # total number of jewelry pieces
    result = total_jewelry
    return result

print(solution())