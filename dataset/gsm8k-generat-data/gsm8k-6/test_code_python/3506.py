def solution():
    # Calculate the amount of change Rosie will get
    change = 1 - 0.44
    # Calculate the number of coins Rosie will get as change
    num_coins = 0
    if change >= 0.25:
        num_coins += 1
        change -= 0.25
    if change >= 0.10:
        num_coins += 1
        change -= 0.10
    if change >= 0.05:
        num_coins += 1
        change -= 0.05
    if change >= 0.01:
        num_coins += 1
        change -= 0.01
    result = num_coins
    return result

print(solution())