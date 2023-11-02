def solution():
    jessica_money = 100  # Jessica has 100 dollars
    ian_money = jessica_money / 2  # Ian has half as much money as Jessica
    rodney_money = ian_money + 35  # Rodney has 35 dollars more than Ian

    # Calculate how much more money Jessica has than Rodney
    difference = jessica_money - rodney_money
    result = difference
    return result

print(solution())