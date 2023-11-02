def solution():
    """A man owned 1/2 of a lot. He sold 1/10 of his share for the amount of $460. What is the worth of the entire lot?"""
    # Define the fraction of the lot owned by the man
    man_fraction = 1/2

    # Calculate the value of the 1/10 of the man's share
    sold_share_value = 460

    # Calculate the value of the entire lot
    lot_value = sold_share_value * (1/man_fraction) * 10

    # Return the result
    result = lot_value
    return result

print(solution())