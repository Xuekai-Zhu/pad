def solution():
    """Eve wants to buy her 3 nieces cooking gear that's made for kids. The hand mitts cost $14.00 and the apron is $16.00. A set of 3 cooking utensils is $10.00 and a small knife is twice the amount of the utensils. The store is offering a 25% off sale on all cooking gear. How much will Eve spend on the gifts?"""
    
    # Define the prices of the cooking gear items
    hand_mitts_price = 14
    apron_price = 16
    utensils_price = 10
    knife_price = 2 * utensils_price
    
    # Calculate the total cost of the cooking gear items before discount
    total_cost_before_discount = (hand_mitts_price + apron_price + 
                                   (utensils_price + knife_price) * 3)
    
    # Calculate the discount amount
    discount = total_cost_before_discount * 0.25
    
    # Calculate the total cost of the cooking gear items after discount
    total_cost_after_discount = total_cost_before_discount - discount
    
    # return the result
    result = total_cost_after_discount
    return result

print(solution())