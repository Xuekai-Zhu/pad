def solution():
    # Define the number of stamps Maria currently has
    current_stamps = 40
    
    # Define the percentage increase she wants
    increase_percentage = 20
    
    # Calculate the total number of stamps she wants to collect
    total_stamps = current_stamps * (1 + increase_percentage/100)
    result = total_stamps
    return result

print(solution())