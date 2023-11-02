def solution():
    """Since Jason started investing, he has earned the same amount he invested twice over in 5 months. If Jason's investment currently is worth $90, how much has he been earning per month from his investment assuming he has been earning an equal amount of returns each month?"""
    investment = 90
    total_return = investment * 2
    months = 5
    monthly_return = total_return / months / 2
    result = monthly_return
    return result

print(solution())