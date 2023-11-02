def solution():
    # Calculate the total amount of money before debts are paid
    total_money = 90 + 48 + 36

    # Calculate the total amount owed after debts are paid
    total_owed = total_money - 28 - 32 - 40

    # Calculate the amount each person will have after debts are paid
    earl_money = 90 - 28 + 40 - (total_owed / 3)
    greg_money = 36 - 32 + (total_owed / 3)

    # Calculate the total amount Greg and Earl will have together
    total_money = earl_money + greg_money
    result = total_money
    return result

print(solution())