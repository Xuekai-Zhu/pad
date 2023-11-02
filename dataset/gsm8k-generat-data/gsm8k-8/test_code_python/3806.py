def solution():
    # Define the cost of jellyfish as x
    x = 1
    
    # Define the cost of eel as 9x
    eel_cost = 9*x
    
    # Calculate the total cost of one order of each kind of sushi
    total_cost = x + eel_cost
    
    # Set the total cost equal to $200
    total_cost = 200
    
    # Solve for x and eel_cost
    x = total_cost / 10
    eel_cost = 9*x
    
    result = eel_cost
    return result

print(solution())