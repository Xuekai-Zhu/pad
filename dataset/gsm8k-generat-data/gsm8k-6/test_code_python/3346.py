def solution():
    # Find the total amount of money Susan spent in September and October
    percent_spent = 1/5 + 1/4
    total_spent = percent_spent * initial_money

    # Find the remaining amount of money after November
    remaining_money = initial_money - total_spent - 120

    # Find the initial amount of money
    initial_money = remaining_money + 540
    result = initial_money
    return result

print(solution())