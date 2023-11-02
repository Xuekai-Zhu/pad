def solution():
    """Devin teaches one math course per year. He taught Calculus for 4 years, Algebra for twice as many years, and Statistics for 5 times as long as he taught Algebra. How many years has Devin taught?"""
    # Define the number of years Devin taught Calculus
    calc_years = 4

    # Define the number of years Devin taught Algebra
    alg_years = calc_years * 2

    # Define the number of years Devin taught Statistics
    stat_years = alg_years * 5

    # Calculate the total number of years Devin has taught
    total_years = calc_years + alg_years + stat_years

    # Return the result
    result = total_years
    return result

print(solution())