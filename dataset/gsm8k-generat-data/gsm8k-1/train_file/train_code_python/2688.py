def solution():
    """Devin teaches one math course per year. He taught Calculus for 4 years, Algebra for twice as many years, and Statistics for 5 times as long as he taught Algebra. How many years has Devin taught?"""
    calculus_years = 4
    algebra_years = calculus_years * 2
    statistics_years = algebra_years * 5
    total_years = calculus_years + algebra_years + statistics_years
    result = total_years
    return result

print(solution())