def solution():
    """Since Jason started investing, he has earned the same amount he invested twice over in 5 months. If Jason's investment currently is worth $90, how much has he been earning per month from his investment assuming he has been earning an equal amount of returns each month?"""
    current_value = 90
    investment = current_value / 3
    months = 5
    earned = current_value - investment
    earnings_per_month = earned / months
    result = earnings_per_month
    return result

print(solution())