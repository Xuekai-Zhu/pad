def solution():
    """Of the 100 soccer balls that Nova went to inflate, 40 percent had holes in them and could not inflate, while 20% of the remaining balls were overinflated and exploded. How many balls were inflated successfully and could be used?"""
    
    # Define the total number of soccer balls that Nova had
    total_balls = 100
    
    # Calculate the number of balls that had holes and could not be inflated
    no_inflate_balls = total_balls * 0.4
    
    # Calculate the remaining number of balls that could be inflated
    inflated_balls = total_balls - no_inflate_balls
    
    # Calculate the number of balls that were overinflated and exploded
    exploded_balls = inflated_balls * 0.2
    
    # Calculate the final number of balls that were successfully inflated and could be used
    success_balls = inflated_balls - exploded_balls
    
    # Display the final number of balls
    result = success_balls
    return result

print(solution())