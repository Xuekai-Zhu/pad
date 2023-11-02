def solution():
    """A gift shop sells bracelets at $15 each, a gold heart necklace at $10,  and a personalized coffee mug at $20.  Raine buys three bracelets, two gold heart necklaces, and one coffee mug for her friends. How much change does Raine get back if she gives a one hundred dollar bill?"""
    # Define the prices of the items
    bracelet_price = 15
    necklace_price = 10
    mug_price = 20

    # Calculate the total cost of the items Raine bought
    total_cost = 3 * bracelet_price + 2 * necklace_price + mug_price

    # Calculate the change Raine will get back
    change = 100 - total_cost

    # return the result
    result = change
    return result

print(solution())