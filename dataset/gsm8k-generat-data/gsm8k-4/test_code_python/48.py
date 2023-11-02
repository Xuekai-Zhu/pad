def solution():
    """Sam memorized six more digits of pi than Carlos memorized. Mina memorized six times as many digits of pi as Carlos memorized. If Mina memorized 24 digits of pi, how many digits did Sam memorize?"""
    # Let's assume that the number of digits that Carlos memorized is "x"
    x = 0

    # Calculate the number of digits that Sam memorized
    sam = x + 6

    # Calculate the number of digits that Mina memorized
    mina = x * 6

    # We know that Mina memorized 24 digits, so we can solve for x
    x = 24 / 6 

    # Calculate the number of digits that Sam memorized using the value of x
    sam = x + 6

    result = sam
    return result

print(solution())