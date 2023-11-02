def solution():
    """Leo and Ryan together have $48. Ryan owns 2/3 of the amount. Leo remembered that Ryan owed him $10 but he also owed Ryan $7. After the debts had been settled, how much money does Leo have?"""
    total_money = 48
    ryan_share = total_money * 2/3
    leo_share = total_money * 1/3
    # After the debts, Ryan owes Leo $3
    ryan_share -= 3
    leo_share += 3
    result = leo_share
    return result

print(solution())