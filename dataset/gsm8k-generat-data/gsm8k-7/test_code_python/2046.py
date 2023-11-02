def solution():
    num_tellers = 4
    num_rolls_per_teller = 10
    num_coins_per_roll = 25
    
    # Calculate the total number of coins per teller
    coins_per_teller = num_rolls_per_teller * num_coins_per_roll
    
    # Calculate the total number of coins for all tellers
    total_coins = num_tellers * coins_per_teller
    result = total_coins
    return result

print(solution())