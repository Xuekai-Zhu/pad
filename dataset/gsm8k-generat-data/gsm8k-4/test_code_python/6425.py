def solution():
    """Bart fills out surveys to earn money. He receives $0.2 for every question he answers in the survey. Each survey has 10 questions. On Monday he finished 3 surveys, and on Tuesday 4 surveys. How much money did he earn during these two days?"""
    # Define the amount earned per survey
    SURVEY_EARNINGS = 2

    # Calculate the total earnings from Monday's surveys
    monday_earnings = SURVEY_EARNINGS * 3 * 10

    # Calculate the total earnings from Tuesday's surveys
    tuesday_earnings = SURVEY_EARNINGS * 4 * 10

    # Calculate the total earnings over the two days
    total_earnings = monday_earnings + tuesday_earnings

    # Convert the total earnings to dollars
    total_earnings = total_earnings / 10

    # return the result
    result = total_earnings
    return result

print(solution())