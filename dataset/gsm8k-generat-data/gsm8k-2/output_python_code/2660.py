def solution():
    """The price of a monster box of cereal is reduced by $24 after an oversupply in the market. If the initial price was $104, and Romina bought 20 of such boxes, calculate the total price she paid."""
    initial_price = 104
    discount = 24
    final_price = initial_price - discount
    num_boxes = 20
    total_price = final_price * num_boxes
    result = total_price
    return result

print(solution())