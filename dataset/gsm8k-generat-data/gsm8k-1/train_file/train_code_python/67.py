def solution():
    """The ratio of coins that Elsa has to that which Amalie has is 10:45. If the total number of coins they have is 440, 
    and Amalie spends 3/4 of what she has on toys, how many will she remain with?"""
    total_coins = 440
    ratio = 10/45 # Elsa : Amalie
    amalie_coins = total_coins * (45/55) # Amalie has 45 out of 55 total coins
    spent_coins = amalie_coins * (3/4) # Amalie spends 3/4 of her coins on toys
    remaining_coins = amalie_coins - spent_coins
    result = remaining_coins
    return result

print(solution())