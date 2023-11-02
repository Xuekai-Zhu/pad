def solution():
    num_records = 200
    sammy_price = 4.0
    bryan_price_interest = 6.0
    bryan_price_not_interest = 1.0
    bryan_interest_num = num_records / 2

    # Calculate the profit from Sammy's deal
    sammy_profit = sammy_price * num_records

    # Calculate the profit from Bryan's deal
    bryan_interest_profit = bryan_price_interest * bryan_interest_num
    bryan_not_interest_profit = bryan_price_not_interest * bryan_interest_num
    bryan_total_profit = bryan_interest_profit + bryan_not_interest_profit

    # Calculate the difference in profit between the two deals
    profit_difference = bryan_total_profit - sammy_profit
    result = profit_difference
    return result

print(solution())