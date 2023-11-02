def solution():
    total_bonus = 1496  # Ben will receive a bonus of $1496
    kitchen_share = total_bonus / 22  # 1/22 of the bonus will go to the kitchen
    holiday_share = total_bonus / 4  # 1/4 of the bonus will go to holidays
    children_share = total_bonus / 8 / 3  # 1/8 of the bonus will go to each of Ben's 3 children

    # Calculate the total expenses
    total_expenses = kitchen_share + holiday_share + children_share

    # Calculate the amount of money left after expenses
    remaining_money = total_bonus - total_expenses
    result = remaining_money
    return result

print(solution())