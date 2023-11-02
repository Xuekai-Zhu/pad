def solution():
    """Jenny has a tummy ache. Her brother Mike says that it is because Jenny ate 5 more than thrice the number of chocolate squares that he ate. If Mike ate 20 chocolate squares, how many did Jenny eat?"""
    mike_squares = 20
    jenny_squares = (mike_squares * 3) + 5
    result = jenny_squares
    return result

print(solution())