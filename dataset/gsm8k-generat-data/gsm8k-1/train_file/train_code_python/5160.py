def solution():
    """Smaug the dragon hoards 100 gold coins, 60 silver coins, and 33 copper coins. If each silver coin is worth 8 copper coins, and each gold coin is worth 3 silver coins, what is the total value of Smaug's hoard expressed as a number of copper coins?"""
    gold_coins = 100
    silver_coins = 60
    copper_coins = 33
    silver_to_copper = 8
    gold_to_silver = 3

    total_copper = (gold_coins * gold_to_silver * silver_to_copper) + (silver_coins * silver_to_copper) + copper_coins
    result = total_copper
    return result

print(solution())