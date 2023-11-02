def solution():
    total_money = 48  # Leo and Ryan have $48 in total
    ryan_money = (2/3) * total_money  # Ryan owns 2/3 of the total money
    leo_money = total_money - ryan_money  # Leo owns the remaining money

    # After the debts have been settled, Leo receives $10 from Ryan but gives back $7 to Ryan
    leo_money += 10 - 7
    result = leo_money
    return result

print(solution())