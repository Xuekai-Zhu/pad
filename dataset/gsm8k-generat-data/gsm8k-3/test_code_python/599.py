def solution():
    """John pays for a candy bar with 4 quarters, 3 dimes, and a nickel.  He got 4 cents back in change.  How many cents did the candy bar cost?"""
    # Define the value of each coin in cents
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5

    # Calculate the total amount paid in cents
    total_paid = 4 * QUARTER_VALUE + 3 * DIME_VALUE + 1 * NICKEL_VALUE

    # Calculate the cost of the candy bar in cents
    cost = total_paid - 4

    # Display the cost of the candy bar
    result = cost
    return result

print(solution())