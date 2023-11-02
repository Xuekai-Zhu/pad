def solution():
    """A jewelry box has 10 necklaces and 15 earrings. Jessy goes to the jewelry stores and buys 10 more necklaces and 2/3 as many earrings as before. After returning home, her mother gives her 1/5 times more earrings than the number she purchased at the store. Calculate the total number of jewelry pieces Jessy has in her box if she puts all of them together."""
    initial_necklaces = 10
    initial_earrings = 15
    extra_necklaces = 10
    extra_earrings = (2/3) * initial_earrings
    total_necklaces = initial_necklaces + extra_necklaces
    total_earrings = initial_earrings + extra_earrings
    mother_bonus = (1/5) * extra_earrings
    total_jewelry = total_necklaces + total_earrings + mother_bonus
    result = total_jewelry
    return result

print(solution())