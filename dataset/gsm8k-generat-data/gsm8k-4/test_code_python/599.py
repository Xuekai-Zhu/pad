def solution():
    """John pays for a candy bar with 4 quarters, 3 dimes, and a nickel. He got 4 cents back in change. How many cents did the candy bar cost?"""
    # Calculate the total value of the quarters used
    quarters_value = 4 * 25

    # Calculate the total value of the dimes used
    dimes_value = 3 * 10

    # Calculate the total value of the nickels used
    nickels_value = 1 * 5

    # Calculate the total amount paid by John
    total_paid = quarters_value + dimes_value + nickels_value

    # Calculate the cost of the candy bar
    candy_bar_cost = total_paid - 4

    result = candy_bar_cost
    return result

print(solution())