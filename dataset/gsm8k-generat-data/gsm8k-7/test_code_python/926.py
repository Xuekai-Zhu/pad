def solution():
    guest_bathroom_sets = 2
    guest_bathroom_price = 40.0
    
    master_bathroom_sets = 4
    master_bathroom_price = 50.0
    
    discount_percentage = 0.2
    
    # Calculate the total cost of all guest bathroom sets
    total_guest_bathroom_cost = guest_bathroom_sets * guest_bathroom_price
    
    # Calculate the total cost of all master bathroom sets
    total_master_bathroom_cost = master_bathroom_sets * master_bathroom_price
    
    # Calculate the total cost of all towel sets before discount
    total_cost_before_discount = total_guest_bathroom_cost + total_master_bathroom_cost
    
    # Calculate the discount amount
    discount_amount = total_cost_before_discount * discount_percentage
    
    # Calculate the total cost of all towel sets after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount
    
    result = total_cost_after_discount
    return result

print(solution())