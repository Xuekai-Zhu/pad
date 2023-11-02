def solution():
    # Total coins put in during first 4 hours
    total_coins = 20 + (30 * 2) + 40

    # Subtract 20 coins borrowed by her mother in hour 5
    coins_left = total_coins - 20
    result = coins_left
    return result

print(solution())