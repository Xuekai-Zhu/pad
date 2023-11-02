def solution():
    
    weekly_investment = 2000
    starting_balance = 250000
    total_investment = weekly_investment * 52
    ending_balance = starting_balance + total_investment
    windfall_amount = 1.5 * ending_balance
    total_amount = ending_balance + windfall_amount
    result = total_amount
    return result

print(solution())