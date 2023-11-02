def solution():
    lottery_winnings = 100
    colin_debt = 20

    # Calculate the amount paid to Helen
    helen_debt = 2 * colin_debt

    # Calculate the amount paid to Benedict
    benedict_debt = helen_debt / 2

    # Calculate the total amount paid towards debts
    total_debt_paid = colin_debt + helen_debt + benedict_debt

    # Calculate the amount of money left after paying off debts
    money_left = lottery_winnings - total_debt_paid
    result = money_left
    return result

print(solution())