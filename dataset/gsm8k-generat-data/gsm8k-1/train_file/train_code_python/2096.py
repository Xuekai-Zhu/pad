def solution():
    """Ali, Nada, and John have a total of $67 in their wallets. Ali has $5 less than Nada and John has 4 times more than Nada. How much money does John have?"""
    total_money = 67
    ali_money = 0
    nada_money = 0
    john_money = 0
    
    # We first need to find the amount of money Ali has
    # Since Ali has $5 less than Nada, we can say Nada's amount is x and Ali's is x-5
    # And since John has 4 times more than Nada, his amount is 4x
    # So we can create an equation to solve for x:
    # x + (x-5) + 4x = 67
    # 6x - 5 = 67
    # 6x = 72
    # x = 12
    
    nada_money = 12
    ali_money = nada_money - 5
    john_money = 4 * nada_money
    
    result = john_money
    return result

print(solution())