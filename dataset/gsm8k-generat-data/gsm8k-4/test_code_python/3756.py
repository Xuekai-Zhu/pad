def solution():
    """Five less than three times the number of Doberman puppies plus the difference between the number of Doberman puppies and the number of Schnauzers is equal to 90. If the number of Doberman puppies is 20, how many Schnauzers are there?"""
    # Define the number of Doberman puppies
    doberman_puppies = 20

    # Define the total value of equation
    equation_value = 90

    # Define the coefficient of the first term in the equation
    coefficient_1 = 3

    # Define the coefficient of the second term in the equation
    coefficient_2 = -1

    # Define the constant in the equation
    constant = 5

    # Define the equation
    equation = coefficient_1*doberman_puppies + coefficient_2*x + constant

    # Solve for the number of Schnauzers
    schnauzers = (equation_value - coefficient_1*doberman_puppies - constant) / coefficient_2

    result = schnauzers
    return result

print(solution())