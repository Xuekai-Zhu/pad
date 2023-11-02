def solution():
    """
    Kathleen receives a weekly allowance for completing all of her chores. During middle school, her allowance was $2 more than $8 but during her senior year, her allowance was $5 more than twice her middle school allowance. What is the percentage increase in Kathleen's weekly allowance?
    """
    middle_school_allowance = 8 + 2
    senior_year_allowance = 5 + 2 * middle_school_allowance
    percentage_increase = ((senior_year_allowance - middle_school_allowance) / 
                            middle_school_allowance) * 100
    result = percentage_increase
    return result

print(solution())