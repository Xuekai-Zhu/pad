def solution():
    """When Erick went to the market to sell his fruits, he realized that the price of lemons had risen by $4 for each lemon. The price of grapes had also increased by half the price that the price of lemon increased by per grape. If he had planned to sell the lemons at $8 and the grapes at $7, and he had 80 lemons and 140 grapes in his basket, how much money did he collect from selling the fruits at the new prices?"""
    lemon_price_increase = 4
    grape_price_increase = lemon_price_increase / 2
    lemon_price_new = 8 + lemon_price_increase
    grape_price_new = 7 + grape_price_increase
    lemons = 80
    grapes = 140
    total_money_collected = (lemons * lemon_price_new) + (grapes * grape_price_new)
    result = total_money_collected
    return result

print(solution())