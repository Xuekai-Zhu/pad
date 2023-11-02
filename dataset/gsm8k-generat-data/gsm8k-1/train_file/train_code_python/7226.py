def solution():
    """Elizabeth has 20 dollars and wants to buy pens and pencils. Each pencil costs $1.60 and each pen cost 2 dollars. How many pencils can she buy with her 20 dollars if she wants 6 pens?"""
    total_money = 20
    pen_cost = 2
    pencil_cost = 1.6
    pens_wanted = 6
    money_spent_on_pens = pen_cost * pens_wanted
    money_remaining = total_money - money_spent_on_pens
    pencils_affordable = money_remaining / pencil_cost
    result = int(pencils_affordable)
    return result

print(solution())