def solution():
    middle_school_allowance = 8 + 2

    senior_year_allowance = (2 * middle_school_allowance) + 5

    increase = senior_year_allowance - middle_school_allowance

    percent_increase = (increase / middle_school_allowance) * 100

    result = percent_increase
    return result

print(solution())