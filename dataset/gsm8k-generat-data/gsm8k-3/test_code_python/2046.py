def solution():
    """Each bank teller has 10 rolls of coins. Each roll has 25 coins. How many coins do four bank tellers have in all?"""
    # Define the number of rolls of coins per bank teller and the number of bank tellers
    ROLLS_PER_TELLER = 10
    TELLERS = 4

    # Calculate the total number of rolls of coins
    total_rolls = ROLLS_PER_TELLER * TELLERS

    # Calculate the total number of coins
    total_coins = total_rolls * 25

    # Display the total number of coins
    result = total_coins
    return result

print(solution())