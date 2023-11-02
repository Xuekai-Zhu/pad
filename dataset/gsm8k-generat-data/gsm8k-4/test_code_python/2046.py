def solution():
    """Each bank teller has 10 rolls of coins. Each roll has 25 coins. How many coins do four bank tellers have in all?"""
    # Define the number of bank tellers and rolls of coins per teller
    NUM_TELLERS = 4
    ROLLS_PER_TELLER = 10

    # Define the number of coins per roll
    COINS_PER_ROLL = 25

    # Calculate the total number of coins
    total_coins = NUM_TELLERS * ROLLS_PER_TELLER * COINS_PER_ROLL

    # Return the result
    result = total_coins
    return result

print(solution())