def solution():
    """A jewelry box has 10 necklaces and 15 earrings. Jessy goes to the jewelry stores and buys 10 more necklaces and 2/3 as many earrings as before. After returning home, her mother gives her 1/5 times more earrings than the number she purchased at the store. Calculate the total number of jewelry pieces Jessy has in her box if she puts all of them together."""
    initial_necklaces = 10
    initial_earrings = 15
    added_necklaces = 10
    added_earrings = (2 / 3) * initial_earrings
    total_necklaces = initial_necklaces + added_necklaces
    total_earrings = initial_earrings + added_earrings
    extra_earrings = (1 / 5) * added_earrings
    total_jewelry = total_necklaces + total_earrings + extra_earrings
    result = total_jewelry
    return result

print(solution())