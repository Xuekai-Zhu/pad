def solution():
    
    middle_school_allowance = 8 + 2
    senior_year_allowance = 5 + 2 * middle_school_allowance
    increase = senior_year_allowance - middle_school_allowance
    percentage_increase = (increase / middle_school_allowance) * 100
    result = percentage_increase
    return result

print(solution())