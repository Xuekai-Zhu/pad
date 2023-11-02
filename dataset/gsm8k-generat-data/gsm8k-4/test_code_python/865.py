def solution():
    """Jenny has a tummy ache. Her brother Mike says that it is because Jenny ate 5 more than thrice the number of chocolate squares that he ate. If Mike ate 20 chocolate squares, how many did Jenny eat?"""
    # Define the number of chocolate squares Mike ate
    mike_chocolates = 20

    # Calculate the number of chocolate squares Jenny ate using the given equation
    jenny_chocolates = 3 * mike_chocolates + 5

    # return the result
    result = jenny_chocolates
    return result

print(solution())