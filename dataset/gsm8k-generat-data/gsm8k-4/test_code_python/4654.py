def solution():
    """Tom and Devin have been teaching for a total of 70 years. Devin has been teaching for 5 less than half the number of years that Tom has. How many years has Tom been teaching?"""
    # Define the total number of years teaching
    total_years = 70

    # Set up equation system to solve for years Tom has been teaching
    # Let x be the number of years Tom has been teaching
    # Let y be the number of years Devin has been teaching
    # We know that x + y = total_years, and y = 0.5x - 5
    # Substituting the second equation into the first, we get 1.5x - 5 = total_years
    # Solving for x, we get x = (total_years + 5) / 1.5
    tom_years = (total_years + 5) / 1.5

    result = tom_years
    return result

print(solution())