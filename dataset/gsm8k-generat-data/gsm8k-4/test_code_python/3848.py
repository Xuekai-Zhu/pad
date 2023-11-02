def solution():
    """James buys 20 coins of a cryptocurrency at $15 each. The value of the coins increases by 2/3. He sells coins to recoup his original investment. How many coins did he sell?"""
    # Define the initial investment and the increase in value
    INITIAL_INVESTMENT = 20 * 15
    VALUE_INCREASE = 2/3

    # Calculate the new value of the coins
    new_value = 15 + 15 * VALUE_INCREASE

    # Calculate the number of coins he needs to sell to recoup his initial investment
    coins_to_sell = INITIAL_INVESTMENT / new_value

    result = round(coins_to_sell)
    return result

print(solution())