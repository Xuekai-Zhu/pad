def solution():
    # Total number of necklaces after buying 10 more
    total_necklaces = 10 + 10

    # Total number of earrings after buying 2/3 as many as before
    total_earrings = 15 + (2/3 * 15)

    # Jessy's mother gives her 1/5 times more earrings
    total_earrings += total_earrings * (1/5)

    # Total number of jewelry pieces
    total_jewelry = total_necklaces + total_earrings
    result = total_jewelry
    return result

print(solution())