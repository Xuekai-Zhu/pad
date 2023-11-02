def solution():
    """5 years ago, a mother was twice as old as her daughter. If the mother is 41 years old now, how old will the daughter be in 3 years?"""
    # Let the daughter's age 5 years ago be x
    # Then the mother's age 5 years ago was 2x
    # Let the daughter's age now be y
    # Then the mother's age now is 2x + 10
    # We know that the mother is 41 now, so 2x + 10 = 41
    # Solving for x, we get x = 15.5
    # Therefore, the daughter's age now is y = x + 5 = 20.5
    # In 3 years, the daughter will be 20.5 + 3 = 23.5

    daughter_age_now = 20.5
    daughter_age_in_3_years = daughter_age_now + 3
    result = daughter_age_in_3_years
    return result

print(solution())