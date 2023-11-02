def solution():
    middle_school_allowance = 8 + 2
    senior_year_allowance = (middle_school_allowance * 2) + 5
    percentage_increase = ((senior_year_allowance - middle_school_allowance) / middle_school_allowance) * 100
    result = percentage_increase
    return result

print(solution())