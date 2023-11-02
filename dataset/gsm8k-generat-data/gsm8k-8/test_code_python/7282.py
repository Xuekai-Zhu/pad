def solution():
    # Calculate the value of Oliver's initial savings
    initial_savings = 40 + 200*0.25

    # Calculate the value of the money he gives to his sister
    money_given = 5 + 120*0.25

    # Calculate the amount of money he is left with
    remaining_money = initial_savings - money_given
    result = remaining_money
    return result

print(solution())