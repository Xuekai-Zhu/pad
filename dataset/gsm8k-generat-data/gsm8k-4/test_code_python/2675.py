def solution():
    """After working for Mrs. Jane, Jason was paid 60 more coins than Jayden. If Jayden received 300 coins, how many coins did Mrs. Jane give to the boys in total?"""
    # Define the amount of coins received by Jayden
    jayden_coins = 300

    # Calculate the amount of coins received by Jason
    jason_coins = jayden_coins + 60

    # Calculate the total amount of coins received by both boys
    total_coins = jayden_coins + jason_coins

    # return the result
    result = total_coins
    return result

print(solution())