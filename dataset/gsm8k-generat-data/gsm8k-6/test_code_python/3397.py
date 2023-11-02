def solution():
    # Calculate the amount of money Ryan owns
    ryan_money = (2/3) * 48

    # Calculate the amount of money Leo owns before debts are settled
    leo_money = 48 - ryan_money

    # Calculate the net amount Leo owns after debts are settled
    net_leo_money = leo_money - 7 + 10

    result = net_leo_money
    return result

print(solution())