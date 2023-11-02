def solution():
    """An old pirate wants to leave his treasure on an island. He has 3500 gold coins. He wants to spread this equally across 5 chests. Additionally, he will put a total of 500 silver coins and twice as many bronze coins as silver, all distributed equally across the chests. How many coins in total will be in each chest?"""
    # Define the number of chests and the total number of gold coins
    NUM_CHESTS = 5
    GOLD_COINS = 3500

    # Calculate the number of gold coins in each chest
    gold_per_chest = GOLD_COINS / NUM_CHESTS

    # Define the number of silver and bronze coins
    SILVER_COINS = 500
    BRONZE_COINS = SILVER_COINS * 2

    # Calculate the total number of silver and bronze coins
    total_silver_bronze = SILVER_COINS + BRONZE_COINS

    # Calculate the number of silver and bronze coins in each chest
    silver_bronze_per_chest = total_silver_bronze / NUM_CHESTS

    # Calculate the total number of coins in each chest
    total_per_chest = gold_per_chest + silver_bronze_per_chest

    # Display the total number of coins in each chest
    result = total_per_chest
    return result

print(solution())