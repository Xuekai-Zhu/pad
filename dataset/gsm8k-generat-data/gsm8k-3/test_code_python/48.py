def solution():
    """Sam memorized six more digits of pi than Carlos memorized. Mina memorized six times as many digits of pi as Carlos memorized. If Mina memorized 24 digits of pi, how many digits did Sam memorize?"""
    # Define the number of digits Carlos memorized
    carlos_digits = None

    # Define the number of digits Sam memorized
    sam_digits = carlos_digits + 6

    # Define the number of digits Mina memorized
    mina_digits = carlos_digits * 6

    # Use Mina's number of digits to solve for Carlos' number of digits
    carlos_digits = mina_digits / 6

    # Use Carlos' number of digits to solve for Sam's number of digits
    sam_digits = carlos_digits + 6

    result = sam_digits
    return result

print(solution())