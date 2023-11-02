def solution():
    """Gretchen has 110 coins. There are 30 more gold coins than silver coins. How many gold coins does Gretchen have?"""
    total_coins = 110
    silver_coins = (total_coins - 30) / 2
    gold_coins = total_coins - silver_coins
    result = gold_coins
    return result

print(solution())