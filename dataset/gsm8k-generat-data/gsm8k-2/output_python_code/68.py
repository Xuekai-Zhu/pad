def solution():
    """The ratio of coins that Elsa has to that which Amalie has is 10:45. If the total number of coins they have is 440, and Amalie spends 3/4 of what she has on toys, how many will she remain with?"""
    total_coins = 440
    elsa_ratio = 10
    amalie_ratio = 45
    total_ratio = elsa_ratio + amalie_ratio
    amalie_coins = (amalie_ratio / total_ratio) * total_coins
    spent_coins = 0.75 * amalie_coins
    remaining_coins = amalie_coins - spent_coins
    result = remaining_coins
    return result

print(solution())