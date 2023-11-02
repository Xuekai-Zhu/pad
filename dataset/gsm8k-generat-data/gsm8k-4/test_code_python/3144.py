def solution():
    """Since Jason started investing, he has earned the same amount he invested twice over in 5 months. If Jason's investment currently is worth $90, how much has he been earning per month from his investment assuming he has been earning an equal amount of returns each month?"""
    # Define the current worth of Jason's investment
    investment_worth = 90

    # Calculate the initial investment
    initial_investment = investment_worth / 3

    # Calculate the total amount earned over 5 months
    total_return = investment_worth - initial_investment

    # Calculate the amount earned per month on average
    monthly_return = total_return / 5

    result = monthly_return
    return result

print(solution())