def solution():
    middle_school_allowance = 8 + 2  # Kathleen's middle school allowance was $2 more than $8
    senior_year_allowance = 5 + (2 * middle_school_allowance)  # Kathleen's senior year allowance was $5 more than twice her middle school allowance

    # Calculate the percentage increase in Kathleen's allowance
    percentage_increase = ((senior_year_allowance - middle_school_allowance) / middle_school_allowance) * 100
    result = percentage_increase
    return result

print(solution())