def solution():
    """5/8 of shoppers at All Goods Available store prefer to avoid the check-out line on weekends and instead go through the express lane. If the number of shoppers in the store is 480, calculate the number of shoppers who pay at the check-out lane."""
    # Define the fraction of shoppers who prefer to use the check-out lane
    checkout_fraction = 3/8

    # Calculate the number of shoppers who prefer to use the express lane
    express_shoppers = 5/8 * 480

    # Calculate the number of shoppers who prefer to use the check-out lane
    checkout_shoppers = checkout_fraction * 480

    # Return the result
    result = checkout_shoppers
    return result

print(solution())