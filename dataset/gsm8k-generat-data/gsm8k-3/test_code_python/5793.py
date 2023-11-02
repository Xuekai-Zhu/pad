def solution():
    """The dog toys Samantha buys for her dog are "buy one get one half off" and all cost $12.00 each. She buys 4 toys.  How much does she spend on dog toys?"""
    # Define the cost of one toy and the discount
    TOY_PRICE = 12.00
    DISCOUNT = 0.5

    # Calculate the cost of two toys after the discount
    discounted_price = TOY_PRICE + (TOY_PRICE * DISCOUNT)
    # Calculate the total cost of four toys
    total_cost = discounted_price * 2 * 2

    # Display the total cost
    result = total_cost
    return result

print(solution())