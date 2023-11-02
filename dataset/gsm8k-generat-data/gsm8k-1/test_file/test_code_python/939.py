def solution():
    """James gets 10 new CDs. Each CD cost $15. He gets them for 40% off. He decides he doesn't like 5 of them and sells them for 40. How much money was he out?"""
    num_cds = 10
    cd_cost = 15
    discount = 40
    sale_price = 40
    total_cost = num_cds * cd_cost * (1 - discount/100)
    money_made = 5 * sale_price
    result = total_cost - money_made
    return result

print(solution())