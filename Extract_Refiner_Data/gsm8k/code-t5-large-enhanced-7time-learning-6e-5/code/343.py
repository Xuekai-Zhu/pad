def solution():
    
    # Define the cost of each shirt and the discount percentage
    SHIRT_COST = 30
    DISCOUNT_PERCENTAGE = 40

    # Calculate the total cost before the discount
    total_cost_before_discount = 2 * SHIRT_COST

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * (DISCOUNT_PERCENTAGE / 100)

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    # Display the total cost after the discount
    result = total_cost_after_discount
    return result

print(solution())