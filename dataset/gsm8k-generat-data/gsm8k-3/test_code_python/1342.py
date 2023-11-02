def solution():
    """James invests $2000 a week into his bank account.  He had $250,000 in his account when the year started.  At the end of the year, he gets a windfall that is worth 50% more than what he has in his bank account.   How much money does he have?"""
    # Define the variables
    weekly_investment = 2000
    starting_balance = 250000
    weeks_in_year = 52
    windfall_multiplier = 1.5

    # Calculate the total amount invested over the year
    total_invested = weekly_investment * weeks_in_year

    # Calculate the ending balance after a year of weekly investments
    ending_balance = starting_balance + total_invested

    # Calculate the windfall amount
    windfall = ending_balance * windfall_multiplier

    # Calculate the total amount of money James has
    total = ending_balance + windfall

    # Display the total amount of money James has
    result = total
    return result

print(solution())