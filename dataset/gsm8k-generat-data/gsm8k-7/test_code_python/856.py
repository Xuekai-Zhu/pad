def solution():
    money_spent_per_month = 2 * 4 # 2 dollars spent per trip, 4 trips per month
    num_months = 12

    # Calculate the total money Randy spent in a year
    total_money_spent = money_spent_per_month * num_months

    # Calculate the initial money Randy had in his piggy bank
    initial_money = total_money_spent + 104
    result = initial_money
    return result

print(solution())