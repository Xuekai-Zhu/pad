def solution():
    cherry_price = 5
    olive_price = 7
    num_bags = 50
    discount = 0.1
    
    # Calculate the total cost before discount
    total_cost = (cherry_price * num_bags) + (olive_price * num_bags)
    
    # Calculate the discount amount
    discount_amount = total_cost * discount
    
    # Calculate the final cost after discount
    final_cost = total_cost - discount_amount
    
    result = final_cost
    return result

print(solution())