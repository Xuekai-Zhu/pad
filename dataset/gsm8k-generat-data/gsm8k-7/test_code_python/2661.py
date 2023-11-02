def solution():
    initial_price = 104
    discount = 24
    new_price = initial_price - discount
    num_boxes = 20

    # Calculate the total cost of all boxes of cereal before discount
    total_cost_before = initial_price * num_boxes

    # Calculate the total cost of all boxes of cereal after discount
    total_cost_after = new_price * num_boxes

    # Calculate the amount saved by Romina due to the discount
    amount_saved = (initial_price - new_price) * num_boxes

    # Calculate the total price paid by Romina
    total_paid = total_cost_after
    result = total_paid
    return result

print(solution())