def solution():
    # Define variables for Rodney, Roger, Ron's lifting capacities
    # Let x be Ron's capacity (in pounds)
    x = 0
    ron_capacity = x
    roger_capacity = 4 * x - 7
    rodney_capacity = 2 * roger_capacity

    # Find the total lifting capacity
    total_capacity = rodney_capacity + roger_capacity + ron_capacity
    
    # Set total_capacity equal to 239 and solve for x
    x = (239 - 2 * roger_capacity) / 5
    
    # Calculate Rodney's capacity using the updated value of x
    roger_capacity = 4 * x - 7
    rodney_capacity = 2 * roger_capacity

    # Return Rodney's capacity (in pounds)
    return rodney_capacity

print(solution())