def solution():
    # Define the number of rolls and coins per roll
    rolls_per_teller = 10
    coins_per_roll = 25

    # Calculate the total number of coins per teller
    coins_per_teller = rolls_per_teller * coins_per_roll

    # Calculate the total number of coins for all four tellers
    total_coins = coins_per_teller * 4
    result = total_coins
    return result

print(solution())