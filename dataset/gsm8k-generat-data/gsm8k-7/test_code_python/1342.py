def solution():
    weekly_investment = 2000
    starting_balance = 250000

    # Calculate the total investment for the year
    total_investment = weekly_investment * 52

    # Calculate the ending balance before the windfall
    ending_balance = starting_balance + total_investment

    # Calculate the value of the windfall
    windfall = ending_balance * 0.5

    # Calculate the final amount of money James has in his account
    final_balance = ending_balance + windfall
    result = final_balance
    return result

print(solution())