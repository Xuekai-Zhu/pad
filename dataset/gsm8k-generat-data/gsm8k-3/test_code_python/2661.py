def solution():
    """The price of a monster box of cereal is reduced by $24 after an oversupply in the market.
    If the initial price was $104, and Romina bought 20 of such boxes, calculate the total price she paid."""
    # Define the initial price and the discount
    INITIAL_PRICE = 104
    DISCOUNT = 24

    # Define the number of boxes bought
    boxes_bought = 20

    # Calculate the total cost before the discount
    total_cost_before_discount = INITIAL_PRICE * boxes_bought

    # Calculate the total cost after the discount
    total_cost_after_discount = (INITIAL_PRICE - DISCOUNT) * boxes_bought

    # Display the total price paid
    result = total_cost_after_discount
    return result

print(solution())