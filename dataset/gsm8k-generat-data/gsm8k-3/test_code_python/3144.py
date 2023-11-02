def solution():
    """Since Jason started investing, he has earned the same amount he invested twice over in 5 months. If Jason's investment currently is worth $90, how much has he been earning per month from his investment assuming he has been earning an equal amount of returns each month?"""
    # Calculate the initial investment amount
    initial_investment = 90 / 3

    # Calculate the amount earned per month
    earning_per_month = initial_investment * 2 / 5

    # Display the earning per month
    result = earning_per_month
    return result

print(solution())