def solution():
    """Allen is 25 years younger than his mother. In 3 years, the sum of their ages will be 41. What is the present age of Allen's mother?"""
    sum_of_ages_in_3_years = 41
    allen_age_in_3_years = x + 3
    mother_age_in_3_years = y + 3
    # We have two equations and two variables, we can solve the system of equations as follows:
    # x + y - 50 = 0
    # x + y + 6 - 41 = 0
    # Solving for y in the first equation, we get y = 50 - x
    # Substituting y in the second equation, we get x + (50 - x) + 6 - 41 = 0
    # Simplifying, we get x = 15
    x = 15
    y = 50 - x
    result = y
    return result

print(solution())