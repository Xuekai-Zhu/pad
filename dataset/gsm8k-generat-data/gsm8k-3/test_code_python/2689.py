def solution():
    """Devin teaches one math course per year. He taught Calculus for 4 years, Algebra for twice as many years, and Statistics for 5 times as long as he taught Algebra. How many years has Devin taught?"""
    # Define the number of years Devin taught Calculus
    calculus_years = 4

    # Define the number of years Devin taught Algebra
    algebra_years = 2 * calculus_years

    # Define the number of years Devin taught Statistics
    statistics_years = 5 * algebra_years

    # Calculate the total number of years Devin taught
    total_years = calculus_years + algebra_years + statistics_years

    # Display the total number of years Devin taught
    result = total_years
    return result

print(solution())