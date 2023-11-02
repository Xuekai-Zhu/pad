def solution():
    """The ratio of coins that Elsa has to that which Amalie has is 10:45. If the total number of coins they have is 440, and Amalie spends 3/4 of what she has on toys, how many will she remain with?"""
    elsa_coins = 10
    amalie_coins = 45
    total_coins = 440
    amalie_spend = 3/4
    amalie_remain = amalie_coins - (amalie_coins * amalie_spend)
    result = amalie_remain
    return result

print(solution())