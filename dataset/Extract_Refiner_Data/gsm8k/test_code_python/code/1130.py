def solution():
    
    # Define the initial savings and the number of weeks
    savings = 4
    weeks = 8

    # Calculate the total savings over the past 8 weeks
    total_savings = savings * weeks

    # Calculate the remaining savings needed to reach $60
    remaining_savings = 60 - total_savings

    # Calculate the number of weeks needed to save the remaining amount
    weeks_needed = remaining_savings / savings

    # Display the number of weeks needed
    result = weeks_needed
    return result

print(solution())