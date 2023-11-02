def solution():
    gold_coins = 100
    silver_coins = 60
    copper_coins = 33
    silver_to_copper = 8
    gold_to_silver = 3
    total_copper = (gold_coins * gold_to_silver * silver_to_copper) + (silver_coins * silver_to_copper) + copper_coins
    result = total_copper
    return result

print(solution())