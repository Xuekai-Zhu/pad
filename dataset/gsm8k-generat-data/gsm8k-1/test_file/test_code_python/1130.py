def solution():
    """Jane has saved $4 of her allowance every week for the past 8 weeks. If she continues to save the same amount each week, how many more weeks will it take for her to have saved a total of $60?"""
    weekly_savings = 4
    total_savings = 60
    weeks_passed = 8
    weeks_needed = (total_savings - (weeks_passed * weekly_savings)) / weekly_savings
    result = weeks_needed
    return result

print(solution())