def solution():
    
    gold_coins = 3500
    silver_coins = 500
    bronze_coins = 2 * silver_coins
    total_coins = gold_coins + silver_coins + bronze_coins
    chests = 5
    coins_per_chest = total_coins // chests
    result = coins_per_chest
    return result

print(solution())