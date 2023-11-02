def solution():
    """Gina had $400. She gave 1/4 of her money to her mom, used 1/8 of her money to buy clothes, gave 1/5 of her money to a charity, and kept the remaining money. How much did Gina keep?"""
    gina_money = 400
    mom_money = gina_money / 4
    clothes_money = gina_money / 8
    charity_money = gina_money / 5

    remaining_money = gina_money - mom_money - clothes_money - charity_money

    result = remaining_money
    return result

print(solution())