def solution():
    # Define the number of boxes and pouches in each box
    num_boxes = 10
    pouches_per_box = 6
    
    # Calculate the total number of pouches
    total_pouches = num_boxes * pouches_per_box
    
    # Convert the total cost to cents
    total_cost = 12 * 100
    
    # Calculate the cost per pouch in cents
    cost_per_pouch = total_cost / total_pouches
    
    # Round the result to the nearest cent
    result = round(cost_per_pouch, 2)
    return result

print(solution())