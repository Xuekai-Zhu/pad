def solution():
    """A pen costs $9 more than a pencil. If a pencil costs $2, find the total cost of both items."""
    
    # Define the cost of a pencil and the cost difference between a pen and a pencil
    PENCIL_COST = 2
    PEN_COST_DIFF = 9
    
    # Calculate the cost of a pen
    pen_cost = PENCIL_COST + PEN_COST_DIFF
    
    # Calculate the total cost of both items
    total_cost = pen_cost + PENCIL_COST
    
    # Display the total cost
    result = total_cost
    return result

print(solution())