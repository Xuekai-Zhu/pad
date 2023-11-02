def solution():
    num_one_dollar_bills = 7
    num_five_dollar_bills = 4
    num_ten_dollar_bills = 2
    num_twenty_dollar_bills = 1

    cost_per_pound = 3
    change_received = 4

    # Calculate the total amount of money Frank has
    total_money = (num_one_dollar_bills * 1) + (num_five_dollar_bills * 5) + \
                  (num_ten_dollar_bills * 10) + (num_twenty_dollar_bills * 20)

    # Calculate the amount of money Frank spends on peanuts
    peanut_cost = total_money - change_received

    # Calculate the total amount of peanuts Frank buys
    total_peanuts = peanut_cost / cost_per_pound

    # Calculate the average pounds of peanuts Frank eats per day
    days_in_week = 7
    average_pounds_per_day = total_peanuts / days_in_week
    result = average_pounds_per_day
    return result

print(solution())