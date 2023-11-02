def solution():
    """Gretchen has some coins. There are 30 more gold coins than silver coins. If she had 70 gold coins, how many coins did Gretchen have in total?"""
    gold_coins = 70
    silver_coins = gold_coins - 30
    total_coins = gold_coins + silver_coins
    result = total_coins
    return result

print(solution())