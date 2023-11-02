def solution():
    """Jude bought three chairs for his house, all at the same price. He also bought a table that costs $50 and two sets of plates at $20 for each set. 
       After giving the cashier $130, Jude got a $4 change. How much did each of the chairs cost?"""
    
    # Define variables
    num_chairs = 3
    table_cost = 50
    plates_cost = 20
    total_paid = 130
    change = 4
    
    # Calculate total cost of table and plates
    total_other_items_cost = table_cost + (2 * plates_cost)
    
    # Calculate total cost of chairs and change received after payment
    total_chair_cost = (total_paid - change - total_other_items_cost) / num_chairs
    
    # Display cost of each chair
    result = total_chair_cost
    return result

print(solution())