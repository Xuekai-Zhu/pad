def solution():
    """John buys 3 barbells and gives $850 and gets $40 in change. How much did each barbell cost?"""
    
    # Define the total amount paid and the amount of change received
    total_paid = 850
    change_received = 40
    
    # Calculate the total cost of the 3 barbells
    total_cost = total_paid - change_received
    cost_per_barbell = total_cost / 3
    
    # Return the cost per barbell
    result = cost_per_barbell
    return result

print(solution())