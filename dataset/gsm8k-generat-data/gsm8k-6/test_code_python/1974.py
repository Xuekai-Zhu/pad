def solution():
    # Calculate Kathleen's middle school allowance
    middle_school_allowance = 8 + 2  # middle school allowance is $2 more than $8

    # Calculate Kathleen's senior year allowance
    senior_year_allowance = 2 * middle_school_allowance + 5  # senior year allowance is $5 more than twice middle school allowance

    # Calculate the percentage increase in Kathleen's allowance
    increase = (senior_year_allowance - middle_school_allowance) / middle_school_allowance * 100

    result = increase
    return result

print(solution())