def solution():
    rolls_per_teller = 10  # Each bank teller has 10 rolls of coins
    coins_per_roll = 25  # Each roll has 25 coins
    number_of_tellers = 4  # There are 4 bank tellers in total

    # Calculate the total number of coins
    total_coins = rolls_per_teller * coins_per_roll * number_of_tellers
    result = total_coins
    return result

print(solution())