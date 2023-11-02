def solution():
    """The ratio of coins that Elsa has to that which Amalie has is 10:45. If the total number of coins they have is 440, and Amalie spends 3/4 of what she has on toys, how many will she remain with?"""
    # Define the ratio of coins that Elsa and Amalie have
    elsa_coins_ratio = 10
    amalie_coins_ratio = 45

    # Calculate the total number of parts in the ratio
    total_ratio = elsa_coins_ratio + amalie_coins_ratio

    # Calculate the fraction of coins that Amalie has
    amalie_fraction = amalie_coins_ratio / total_ratio

    # Calculate the total number of coins that Amalie has
    total_coins = 440
    amalie_coins = total_coins * amalie_fraction

    # Calculate the amount Amalie spends on toys
    toys_spending = amalie_coins * (3/4)

    # Calculate the number of coins Amalie will have left after buying toys
    amalie_coins_left = amalie_coins - toys_spending

    # Return the result
    result = amalie_coins_left
    return result

print(solution())