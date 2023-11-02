def solution():
    iphone_cost = 800
    trade_in_value = 240
    weekly_earnings = 80

    # Calculate the total amount Carrie will have after trading in her Samsung Galaxy
    total_after_trade_in = iphone_cost - trade_in_value

    # Calculate the number of weeks Carrie needs to save up for the remaining amount
    num_weeks = total_after_trade_in / weekly_earnings
    result = num_weeks
    return result

print(solution())