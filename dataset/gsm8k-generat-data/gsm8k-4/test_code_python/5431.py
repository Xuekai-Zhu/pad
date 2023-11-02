def solution():
    """Felicity and Adhira took separate trips. Felicity used 5 less gallons of gas than four times the number of gallons that Adhira used for her trip. Together the girls used 30 gallons of gas. How many gallons did Felicity use?"""
    # Define the number of gallons Adhira used
    adhira_gallons = None
    
    # Define the number of gallons Felicity used
    felicity_gallons = None
    
    # Using the given information, create a system of equations
    # First equation: felicity_gallons = 4 * adhira_gallons - 5
    # Second equation: felicity_gallons + adhira_gallons = 30
    
    # Substituting the first equation into the second equation, we get:
    # (4 * adhira_gallons - 5) + adhira_gallons = 30
    
    # Solving for adhira_gallons, we get:
    adhira_gallons = 7.5
    
    # Substituting adhira_gallons into the first equation, we get:
    felicity_gallons = 27
    
    # Return the number of gallons Felicity used
    result = felicity_gallons
    return result

print(solution())