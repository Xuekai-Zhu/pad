def solution():
    """James buys 20 coins of a cryptocurrency at $15 each. The value of the coins increases by 2/3. He sells coins to recoup his original investment. How many coins did he sell?"""
    initial_investment = 20 * 15
    increased_value = (2 / 3) * 15
    new_value = 15 + increased_value
    number_of_coins_sold = initial_investment / new_value
    result = number_of_coins_sold
    return result

print(solution())