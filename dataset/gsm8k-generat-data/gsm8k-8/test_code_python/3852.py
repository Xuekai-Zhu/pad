def solution():
    # Calculate the total number of ball bearings needed
    total_bearings = 10 * 30

    # Calculate the total cost without any discounts
    cost_without_discount = total_bearings * 1

    # Calculate the total cost with the sale discount
    cost_with_sale_discount = total_bearings * 0.75

    # Calculate the total cost with the bulk discount
    cost_with_bulk_discount = cost_with_sale_discount * 0.8

    # Calculate the amount saved by buying during the sale
    amount_saved = cost_without_discount - cost_with_bulk_discount

    result = amount_saved
    return result

print(solution())