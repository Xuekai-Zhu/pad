def solution():
    # Define the amount James invests and his starting account balance
    weekly_investment = 2000
    starting_balance = 250000

    # Calculate James' end-of-year account balance
    year_total_investment = weekly_investment * 52
    end_of_year_balance = starting_balance + year_total_investment

    # Calculate the value of the windfall
    windfall_value = 1.5 * end_of_year_balance

    # Calculate James' total money at the end of the year
    total_money = end_of_year_balance + windfall_value
    result = total_money
    return result

print(solution())