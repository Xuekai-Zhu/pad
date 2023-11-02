def solution():
    """Janet pays $40/hour for 3 hours per week of clarinet lessons and $28/hour for 5 hours a week of piano lessons. How much more does she spend on piano lessons than clarinet lessons in a year?"""
    
    # Calculate the total cost of clarinet lessons per week
    clarinet_cost = 40 * 3
    
    # Calculate the total cost of piano lessons per week
    piano_cost = 28 * 5
    
    # Calculate the cost difference between piano and clarinet lessons per week
    weekly_cost_diff = piano_cost - clarinet_cost
    
    # Calculate the yearly cost difference
    yearly_cost_diff = weekly_cost_diff * 52
    
    # Display the yearly cost difference
    result = yearly_cost_diff
    return result

print(solution())