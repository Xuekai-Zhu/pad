def solution():
    cost_per_coffee = 2  # John used to buy 4 coffees a day for $2 each
    new_cost_per_coffee = cost_per_coffee * 1.5  # Coffee price went up by 50%
    new_num_coffees = 2  # John now buys 2 coffees a day

    # Calculate John's old daily coffee expense
    old_daily_expense = cost_per_coffee * 4

    # Calculate John's new daily coffee expense
    new_daily_expense = new_cost_per_coffee * 2

    # Calculate the amount of money John saves per day compared to what he used to spend
    money_saved_per_day = old_daily_expense - new_daily_expense
    result = money_saved_per_day
    return result

print(solution())