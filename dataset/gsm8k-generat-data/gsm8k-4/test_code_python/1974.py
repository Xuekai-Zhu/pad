def solution():
    """Kathleen receives a weekly allowance for completing all of her chores. During middle school, her allowance was $2 more than $8 but during her senior year, her allowance was $5 more than twice her middle school allowance. What is the percentage increase in Kathleen's weekly allowance?"""
    # Define the middle school allowance and senior year allowance
    ms_allowance = 8 + 2
    sr_allowance = 5 + 2 * ms_allowance

    # Calculate the percentage increase in Kathleen's weekly allowance
    percentage_increase = ((sr_allowance - ms_allowance) / ms_allowance) * 100

    # Round the result to 2 decimal places
    result = round(percentage_increase, 2)
    return result

print(solution())