def solution():
    """Amy, Jeremy, and Chris have a combined age of 132. Amy is 1/3 the age of Jeremy, and Chris is twice as old as Amy. How old is Jeremy?"""
    # Define the variables for the ages
    amy_age = None
    jeremy_age = None
    chris_age = None

    # Define the total combined age
    total_age = 132

    # Set up the equations for the ages
    # Amy is 1/3 the age of Jeremy
    amy_age = jeremy_age / 3
    # Chris is twice as old as Amy
    chris_age = amy_age * 2
    # The total age is the sum of their ages
    total_age_equation = amy_age + jeremy_age + chris_age

    # Define the equation solver function
    def solve_equations():
        nonlocal amy_age
        nonlocal jeremy_age
        nonlocal chris_age
        nonlocal total_age_equation

        # Solve for Jeremy's age using the total_age equation
        jeremy_age = (total_age - chris_age) / (1 + 1/3)
        # Solve for Amy's age using the equation for Amy's age
        amy_age = jeremy_age / 3
        # Solve for Chris's age using the equation for Chris's age
        chris_age = amy_age * 2
        # Recalculate the total age using the solved ages
        total_age_equation = amy_age + jeremy_age + chris_age

    # Use the equation solver function to find the ages that satisfy the conditions
    while total_age_equation != total_age:
        solve_equations()

    # The solution is Jeremy's age
    result = jeremy_age
    return result

print(solution())