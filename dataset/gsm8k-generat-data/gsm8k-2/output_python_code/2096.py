def solution():
    """Ali, Nada, and John have a total of $67 in their wallets. Ali has $5 less than Nada and John has 4 times more than Nada. How much money does John have?"""
    total_money = 67
    john_ratio = 4
    nada_money = total_money / (1 + 1 + john_ratio)
    ali_money = nada_money - 5
    john_money = nada_money * john_ratio
    result = john_money
    return result

print(solution())