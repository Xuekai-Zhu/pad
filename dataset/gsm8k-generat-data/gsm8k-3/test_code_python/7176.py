def solution():
    """Tate finishes high school in 1 year less than normal. It takes him 3 times that long to get his bachelor's degree and Ph.D. How many years did he spend in high school and college?"""
    # Let x be the normal time to finish high school
    x = 4
    # Tate finishes high school in 1 year less than normal
    hs_years = x - 1
    # It takes Tate 3 times that long to get his bachelor's degree and Ph.D.
    college_years = 3 * (x + hs_years)

    # Total years spent in high school and college
    total_years = hs_years + college_years

    # Display the total years
    result = total_years
    return result

print(solution())