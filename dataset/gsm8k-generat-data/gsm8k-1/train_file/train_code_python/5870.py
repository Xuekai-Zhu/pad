def solution():
    """Tayzia and her two young daughters get haircuts. Women’s haircuts are $48. Children’s haircuts are $36. If Tayzia wants to give a 20% tip to the hair stylist, how much would it be?"""
    women_haircuts = 1
    children_haircuts = 2
    women_price = 48
    children_price = 36
    total_price = women_haircuts * women_price + children_haircuts * children_price
    tip_percent = 20
    tip_amount = total_price * (tip_percent / 100)
    result = tip_amount
    return result

print(solution())