def solution():
    """A shipping boat's crew consisted of 17 sailors, with five inexperienced sailors. Each experienced sailor was paid 1/5 times more than the inexperienced sailors. If the inexperienced sailors were paid $10 per hour for a 60-hour workweek, calculate the total combined monthly earnings of the experienced sailors."""
    
    # Define the number of inexperienced sailors and their hourly rate
    num_inexperienced = 5
    inexperienced_rate = 10
    
    # Calculate the hourly rate for experienced sailors
    experienced_rate = inexperienced_rate * (1 + 1/5)
    
    # Calculate the total number of experienced sailors
    num_experienced = 17 - num_inexperienced
    
    # Calculate the total combined earnings of the experienced sailors for a 60-hour workweek
    total_experienced_earnings = num_experienced * experienced_rate * 60
    
    # Calculate the total combined monthly earnings of the experienced sailors (assuming 4 weeks in a month)
    total_monthly_earnings = total_experienced_earnings * 4
    
    # Display the total combined monthly earnings of the experienced sailors
    result = total_monthly_earnings
    return result

print(solution())