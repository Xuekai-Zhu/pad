def solution():
    total_money = 48
    ryan_own = (2/3) * total_money
    leo_own = total_money - ryan_own
    ryan_owe_leo = 10
    leo_owe_ryan = 7

    # After the debts are settled, calculate how much money Leo has left
    leo_own -= leo_owe_ryan
    ryan_own -= ryan_owe_leo
    total_money = leo_own + ryan_own
    result = total_money
    return result

print(solution())