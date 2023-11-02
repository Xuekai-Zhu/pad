def solution():
    """John buys cans of soup for buy 1 get one free.  He gets 30 cans with a normal price of $0.60.  How much does he pay?"""
    # Define the regular price per can of soup
    REGULAR_PRICE = 0.60

    # Define the number of cans of soup purchased
    cans_purchased = 30

    # Calculate the number of cans John actually pays for
    actual_cans_purchased = cans_purchased / 2

    # Calculate the total cost of the soup cans
    total_cost = actual_cans_purchased * REGULAR_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())