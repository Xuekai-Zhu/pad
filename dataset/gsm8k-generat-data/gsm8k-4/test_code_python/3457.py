def solution():
    """An old pirate wants to leave his treasure on an island. He has 3500 gold coins. He wants to spread this equally across 5 chests. Additionally, he will put a total of 500 silver coins and twice as many bronze coins as silver, all distributed equally across the chests. How many coins in total will be in each chest?"""
    # Define the numbers of chests
    NUM_CHESTS = 5

    # Calculate the number of gold coins per chest
    gold_coins = 3500 // NUM_CHESTS

    # Calculate the number of silver coins per chest
    silver_coins = 500 // NUM_CHESTS

    # Calculate the number of bronze coins per chest
    bronze_coins = (2 * silver_coins) // NUM_CHESTS

    # Calculate the total number of coins per chest
    total_coins = gold_coins + silver_coins + bronze_coins

    # return the result
    result = total_coins
    return result

print(solution())