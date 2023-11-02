def solution():
    num_coins = 10
    frappuccino_cost = 3
    remaining_money = 11

    # Since a loonie is worth $1 and a toonie is worth $2, we can set up the equation:
    # x + y = num_coins (total number of coins)
    # x + 2y = remaining_money + frappuccino_cost (total value of coins after buying the Frappuccino)
    # Then we can solve for y (the number of toonies) using substitution
    y = (remaining_money + frappuccino_cost - num_coins) / 1
    result = y
    return result

print(solution())