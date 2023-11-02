def solution():
    # Count the initial number of each coin
    dimes = 2
    quarters = 6
    nickels = 5

    # Add the coins given by Linda's mother
    dimes += 2
    quarters += 10
    nickels += 2 * 5

    # Calculate the total number of coins
    total_coins = dimes + quarters + nickels
    result = total_coins
    return result

print(solution())