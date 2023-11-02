def solution():
    # Find the number of years Tate spent in high school
    high_school_years = normal_high_school_years - 1  # Tate finished high school in 1 year less than normal

    # Find the number of years Tate spent in college (bachelor's degree and Ph.D)
    college_years = 3 * normal_high_school_years  # it takes Tate 3 times the length of high school to get his bachelor's and Ph.D degrees

    # Find the total number of years Tate spent in high school and college
    total_years = high_school_years + college_years
    result = total_years
    return result

print(solution())