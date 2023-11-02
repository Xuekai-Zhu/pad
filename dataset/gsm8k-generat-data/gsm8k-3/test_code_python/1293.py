def solution():
    """Jimmy and Irene go shopping for clothes on a Tuesday, where senior citizens get a 10% discount on their purchases.  Jimmy picks out 3 shorts from the $15 rack.  Irene grabs 5 shirts from the $17 rack.  How much money do they give to the cashier?"""
    # Define the prices and quantities of the items purchased
    short_price = 15
    shirt_price = 17
    num_shorts = 3
    num_shirts = 5

    # Calculate the total cost before the discount
    total_cost = (short_price * num_shorts) + (shirt_price * num_shirts)

    # Calculate the amount of the discount
    discount = 0.1 * total_cost

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost - discount

    # Display the total cost after the discount
    result = total_cost_after_discount
    return result

print(solution())