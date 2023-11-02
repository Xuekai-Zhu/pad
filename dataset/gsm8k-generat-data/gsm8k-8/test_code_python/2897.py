def solution():
    # Calculate the cost of one bottle of sunscreen
    cost_per_bottle = 30.00

    # Calculate the cost of 12 bottles of sunscreen without the discount
    total_cost_without_discount = 12 * cost_per_bottle

    # Calculate the discount
    discount_percentage = 30
    discount_amount = total_cost_without_discount * (discount_percentage / 100)

    # Calculate the total cost with the discount
    total_cost_with_discount = total_cost_without_discount - discount_amount
    
    result = total_cost_with_discount
    return result

print(solution())