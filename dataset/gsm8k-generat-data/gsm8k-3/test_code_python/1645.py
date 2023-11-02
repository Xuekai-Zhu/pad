def solution():
    """A gift shop sells bracelets at $15 each, a gold heart necklace at $10,  and a personalized coffee mug at $20.  Raine buys three bracelets, two gold heart necklaces, and one coffee mug for her friends. How much change does Raine get back if she gives a one hundred dollar bill?"""
    # Define the prices of each item
    BRACELET_PRICE = 15
    NECKLACE_PRICE = 10
    MUG_PRICE = 20

    # Define the quantity of each item purchased
    num_bracelets = 3
    num_necklaces = 2
    num_mugs = 1

    # Calculate the total cost of the items
    total_cost = (num_bracelets * BRACELET_PRICE) + (num_necklaces * NECKLACE_PRICE) + (num_mugs * MUG_PRICE)

    # Calculate the change from a $100 bill
    change = 100 - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())