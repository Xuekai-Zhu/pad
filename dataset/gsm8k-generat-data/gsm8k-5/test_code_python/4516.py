def solution():
    original_order = 25  # Ian's original order was $25
    new_order = original_order + 2.20 + 1.75 + 0.04  # Ian's new order with the substitutes

    # Calculate the difference in cost between the original and new orders
    cost_difference = new_order - original_order

    # Calculate Ian's total bill, including delivery and tip
    total_bill = new_order + 8

    result = total_bill
    return result

print(solution())