def solution():
    """Ali has four $10 bills and six $20 bills that he saved after working for Mr. James on his farm. Ali gives her sister half of the total money he has and uses 3/5 of the remaining amount of money to buy dinner. Calculate the amount of money he has after buying the dinner."""
    num_10_bills = 4
    num_20_bills = 6
    total_money = (num_10_bills*10) + (num_20_bills*20)
    half_money = total_money/2
    remaining_money = total_money - half_money
    money_spent = (3/5) * remaining_money
    money_left = remaining_money - money_spent
    result = money_left
    return result

print(solution())