def solution():
    """John buys dinner plates and silverware. The silverware cost $20. 
    The dinner plates cost 50% as much as the silverware. How much did he pay for everything?"""
    
    # Define the cost of the silverware
    silverware_cost = 20
    
    # Calculate the cost of the dinner plates
    dinner_plate_cost = silverware_cost * 0.5
    
    # Calculate the total cost
    total_cost = silverware_cost + dinner_plate_cost
    
    # Display the total cost
    result = total_cost
    return result

print(solution())