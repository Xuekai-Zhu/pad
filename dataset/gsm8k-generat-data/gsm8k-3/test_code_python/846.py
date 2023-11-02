def solution():
    """Kurt's old refrigerator cost $0.85 a day in electricity. He recently bought a new energy-efficient refrigerator that only cost $0.45 a day in electricity. How much money does Kurt save in a 30-day month with his new refrigerator?"""
    
    # Define the cost of electricity per day for the old and new refrigerators
    OLD_COST = 0.85
    NEW_COST = 0.45
    
    # Calculate the cost difference per day
    cost_difference = OLD_COST - NEW_COST
    
    # Calculate the total cost difference for a 30-day month
    savings = cost_difference * 30
    
    # Display the amount of money Kurt saves
    result = savings
    return result

print(solution())