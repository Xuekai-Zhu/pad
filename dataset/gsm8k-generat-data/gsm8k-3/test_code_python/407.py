def solution():
    """Eustace is twice as old as Milford. In 3 years, he will be 39. How old will Milford be?"""
    # Set up equation with variables representing Milford's age and Eustace's age
    # Eustace = 2 * Milford
    # Eustace + 3 = 39 (in 3 years)
    # Substituting the first equation into the second equation we get
    # 2 * Milford + 3 = 39
    # Solving for Milford's age in 3 years
    milford_age_3_years = (39 - 3) / 2
    # Subtracting 3 years from Milford's age in 3 years to get his current age
    milford_age = milford_age_3_years - 3
    result = milford_age
    return result

print(solution())