def solution():
    num_10_bills = 4
    num_20_bills = 6

    # Calculate the total amount of money Ali has
    total_money = (num_10_bills * 10) + (num_20_bills * 20)

    # Calculate the amount of money Ali gives to her sister
    sister_money = total_money / 2

    # Calculate the remaining amount of money
    remaining_money = total_money - sister_money

    # Calculate the amount of money Ali uses to buy dinner
    dinner_money = remaining_money * (3/5)

    # Calculate the amount of money Ali has after buying dinner
    money_after_buying_dinner = remaining_money - dinner_money
    result = money_after_buying_dinner
    return result

print(solution())