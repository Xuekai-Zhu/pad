def solution():
    # Calculate the total number of coins Tina puts in the jar
    total_coins = 20 + (30 * 2) + 40

    # Take out the 20 coins that Tina's mother borrowed
    remaining_coins = total_coins - 20
    result = remaining_coins
    return result

print(solution())