def solution():
    gold_coins = 3500
    silver_coins = 500
    bronze_coins = silver_coins * 2
    total_coins = gold_coins + silver_coins + bronze_coins
    coins_per_chest = total_coins / 5
    result = coins_per_chest
    return result

print(solution())