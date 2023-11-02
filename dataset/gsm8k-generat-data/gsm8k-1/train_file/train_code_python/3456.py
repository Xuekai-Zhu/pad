def solution():
    """An old pirate wants to leave his treasure on an island. He has 3500 gold coins. He wants to spread this equally across 5 chests. Additionally, he will put a total of 500 silver coins and twice as many bronze coins as silver, all distributed equally across the chests. How many coins in total will be in each chest?"""
    gold_coins = 3500
    chests = 5
    gold_per_chest = gold_coins // chests

    silver_coins = 500
    bronze_coins = silver_coins * 2
    total_coins = gold_coins + silver_coins + bronze_coins
    coins_per_chest = total_coins // chests

    result = coins_per_chest
    return result

print(solution())