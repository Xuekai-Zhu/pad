def solution():
    # Define variables for number of digits each person memorized
    carlos_digits = x
    sam_digits = x + 6
    mina_digits = 6 * x

    # Use Mina's digits to solve for x
    x = mina_digits / 6

    # Calculate how many digits Sam memorized
    sam_digits = x + 6
    result = sam_digits
    return result

print(solution())