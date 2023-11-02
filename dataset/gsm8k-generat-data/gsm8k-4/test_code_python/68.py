def solution():
    """The ratio of coins that Elsa has to that which Amalie has is 10:45. If the total number of coins they have is 440, and Amalie spends 3/4 of what she has on toys, how many will she remain with?"""
    # Define the ratio of coins Elsa has to Amalie
    elsa_amalie_ratio = 10/45

    # Calculate the total number of coins they have
    total_coins = 440

    # Calculate the total number of coins Amalie has
    amalie_coins = total_coins / (1 + elsa_amalie_ratio)

    # Calculate the amount Amalie spends on toys
    toy_spending = amalie_coins * (3/4)

    # Calculate the number of coins Amalie remains with
    amalie_coins_remaining = amalie_coins - toy_spending

    result = amalie_coins_remaining
    return result

print(solution())