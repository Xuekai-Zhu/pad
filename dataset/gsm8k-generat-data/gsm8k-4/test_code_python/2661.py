def solution():
    """The price of a monster box of cereal is reduced by $24 after an oversupply in the market. If the initial price was $104, and Romina bought 20 of such boxes, calculate the total price she paid."""
    # Define the initial price and the discount
    initial_price = 104
    discount = 24

    # Calculate the final price after the discount
    final_price = initial_price - discount

    # Calculate the total price paid by Romina for 20 boxes
    total_price = final_price * 20

    result = total_price
    return result

print(solution())