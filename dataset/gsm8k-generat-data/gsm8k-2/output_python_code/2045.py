def solution():
    """Each bank teller has 10 rolls of coins. Each roll has 25 coins. How many coins do four bank tellers have in all?"""
    rolls_per_teller = 10
    coins_per_roll = 25
    total_tellers = 4
    total_coins = rolls_per_teller * coins_per_roll * total_tellers
    result = total_coins
    return result

print(solution())