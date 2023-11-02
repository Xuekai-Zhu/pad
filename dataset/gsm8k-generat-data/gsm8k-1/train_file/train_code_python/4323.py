def solution():
    """Carmela has $7 and each of her four cousins has $2. How much will Carmela have to give to each of her cousins so that she and her cousins will have the same amount of money?"""
    carmela_money = 7
    cousin_money = 2
    total_cousins = 4
    total_money = carmela_money + (cousin_money * total_cousins)
    equal_money = total_money / (total_cousins + 1)
    money_to_give = carmela_money - equal_money
    result = round(money_to_give, 2)
    return result

print(solution())