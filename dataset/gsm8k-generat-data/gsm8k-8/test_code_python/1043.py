def solution():
    # Calculate the total cost before discount
    total_cost = 2500 + 3500 + 2000

    # Calculate the discount amount
    discount_amount = total_cost * 0.1

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount_amount

    result = total_cost_after_discount
    return result

print(solution())