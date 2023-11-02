def solution():
    """Tom and Devin have been teaching for a total of 70 years. Devin has been teaching for 5 less than half the number of years that Tom has. How many years has Tom been teaching?"""
    total_years = 70
    devin_years = (1/2)*tom_years - 5
    tom_years = total_years - devin_years
    result = tom_years
    return result

print(solution())