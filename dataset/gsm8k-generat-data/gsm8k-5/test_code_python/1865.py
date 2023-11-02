def solution():
    # Initial coins
    dimes = 2
    quarters = 6
    nickels = 5

    # Coins given by Linda's mother
    dimes += 2
    quarters += 10
    nickels *= 2

    # Total number of coins
    total_coins = dimes + quarters + nickels
    result = total_coins
    return result

print(solution())