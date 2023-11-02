def solution():
    # Jake starts with 80 bitcoins
    jakes_coins = 80

    # Jake donates 20 bitcoins to charity
    jakes_coins -= 20

    # Jake gives half of his remaining coins to his brother
    jakes_coins /= 2

    # Jake triples the number of coins he has
    jakes_coins *= 3

    # Jake donates another 10 bitcoins
    jakes_coins -= 10

    result = jakes_coins
    return result

print(solution())