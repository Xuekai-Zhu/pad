def solution():
    num_chests = 5
    gold_coins = 3500
    silver_coins = 500
    bronze_coins = 2 * silver_coins  # twice as many bronze coins as silver
    total_coins = gold_coins + silver_coins + bronze_coins

    # Calculate the number of coins in each chest
    coins_per_chest = total_coins // num_chests
    result = coins_per_chest
    return result

print(solution())