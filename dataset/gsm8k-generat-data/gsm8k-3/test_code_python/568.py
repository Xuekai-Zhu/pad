def solution():
    """John pays for half the cost of raising a child.  It cost $10,000 a year for the first 8 years and then twice that much per year until the child is 18. University tuition then costs $250,000. How much did it cost?"""
    # Calculate the cost of raising the child before university
    cost_before_university = 0
    for year in range(1, 19):
        if year <= 8:
            cost_before_university += 10000
        else:
            cost_before_university += 20000
    
    # Calculate the total cost of raising the child
    total_cost = cost_before_university + 250000
    
    # Calculate John's half of the total cost
    john_half = total_cost / 2
    
    # Display John's half of the total cost
    result = john_half
    return result

print(solution())