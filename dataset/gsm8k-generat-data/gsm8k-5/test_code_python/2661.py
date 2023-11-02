def solution():
    initial_price = 104  # The initial price of a box of cereal
    reduction = 24  # The reduction in price for each box of cereal
    final_price = initial_price - reduction  # The final price of a box of cereal after reduction
    boxes = 20  # The number of boxes Romina bought

    # Calculate the total price Romina paid
    total_price = final_price * boxes
    result = total_price
    return result

print(solution())