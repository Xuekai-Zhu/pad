def solution():
    
    # Define the prices of the items
    pot_price = 120
    mixing_bowl_price = 20
    utenils_price = 5

    # Calculate the total cost of the items before the discount
    total_cost_before_discount = pot_price + mixing_bowl_price + utenils_price

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * 0.2

    # Calculate the total cost of the items after the discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    # Display the total cost after the discount
    result = total_cost_after_discount
    return result

print(solution())