def solution():
    # Define the cost and quantity of the variety pack
    pack_cost = 40.00
    pack_quantity = 4
    
    # Calculate the cost of rush shipping
    rush_cost = pack_cost * 0.30
    
    # Calculate the total cost of the order
    total_cost = pack_cost + rush_cost
    
    # Calculate the cost per pack of sliced meat
    sliced_meat_cost = total_cost / pack_quantity
    
    result = sliced_meat_cost
    return result

print(solution())