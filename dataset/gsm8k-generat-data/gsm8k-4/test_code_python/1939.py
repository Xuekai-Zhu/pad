def solution():
    """Half of Jerome's money was $43. He gave $8 to Meg and thrice as much to Bianca. How much does Jerome have left?"""
    # Define the initial amount of money Jerome had
    initial_money = 2 * 43

    # Calculate how much money Jerome gave to Meg
    jerome_money_left = initial_money - 8

    # Calculate how much money Jerome gave to Bianca
    bianca_money = 3 * 8
    jerome_money_left -= bianca_money

    result = jerome_money_left
    return result

print(solution())