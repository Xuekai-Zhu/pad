def solution():
    # Define the number of classes and whiteboards
    num_classes = 5
    num_whiteboards_per_class = 2
    
    # Define the amount of ink used per whiteboard per day
    ink_per_whiteboard_per_day = 20 # ml
    
    # Define the cost of ink per ml
    ink_cost_per_ml = 0.5 # dollars
    
    # Calculate the total amount of ink used per day
    total_ink_per_day = num_classes * num_whiteboards_per_class * ink_per_whiteboard_per_day
    
    # Calculate the cost of ink for one day's use of the whiteboards
    ink_cost_per_day = total_ink_per_day * ink_cost_per_ml
    
    result = ink_cost_per_day
    return result

print(solution())