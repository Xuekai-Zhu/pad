def solution():
    weekly_investment = 2000  # James invests $2000 a week
    starting_balance = 250000  # James had $250,000 in his account when the year started
    weeks_in_year = 52  # There are 52 weeks in a year

    # Calculate James' ending balance after 1 year of weekly investments
    ending_balance = starting_balance + (weekly_investment * weeks_in_year)

    # Calculate the windfall amount
    windfall = ending_balance * 1.5

    # Calculate James' total amount of money after the windfall
    total_money = ending_balance + windfall
    result = total_money
    return result

print(solution())