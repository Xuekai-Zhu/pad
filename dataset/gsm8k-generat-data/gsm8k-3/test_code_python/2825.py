def solution():
    """A man owned 1/2 of a lot. He sold 1/10 of his share for the amount of $460. What is the worth of the entire lot?"""
    # Define the fraction of the lot owned by the man
    MAN_SHARE = 1/2

    # Define the fraction of the man's share sold for $460
    SOLD_SHARE = 1/10 * MAN_SHARE

    # Calculate the value of the sold share
    sold_value = 460

    # Calculate the value of the whole lot
    lot_value = sold_value / SOLD_SHARE

    # Display the value of the whole lot
    result = lot_value
    return result

print(solution())