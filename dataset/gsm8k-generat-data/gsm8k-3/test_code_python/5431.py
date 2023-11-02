def solution():
    """Felicity and Adhira took separate trips. Felicity used 5 less gallons of gas than four times the number of gallons that Adhira used for her trip. Together the girls used 30 gallons of gas.  How many gallons did Felicity use?"""
    # Let x be the number of gallons Adhira used
    # Then the number of gallons Felicity used is 4x - 5

    # Set up the equation for the total number of gallons used
    x + (4x-5) = 30

    # Simplify and solve for x
    5x - 5 = 30
    5x = 35
    x = 7

    # Calculate the number of gallons Felicity used
    felicity_gallons = 4*x - 5

    # Display the number of gallons Felicity used
    result = felicity_gallons
    return result

print(solution())