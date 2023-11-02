def solution():
    """A gold coin is worth 50 dollars and a silver coin is worth 25 dollars. If you have 3 gold coins, 5 silver coins, and 30 dollars cash, how much money do you have in dollars?"""
    gold_value = 50
    silver_value = 25
    gold_coins = 3
    silver_coins = 5
    cash = 30
    total_value = gold_value * gold_coins + silver_value * silver_coins + cash
    result = total_value
    return result

print(solution())