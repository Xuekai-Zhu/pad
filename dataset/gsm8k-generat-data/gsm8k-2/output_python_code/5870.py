def solution():
    """Tayzia and her two young daughters get haircuts. Women’s haircuts are $48. Children’s haircuts are $36. If Tayzia wants to give a 20% tip to the hair stylist, how much would it be?"""
    women_haircut_price = 48
    children_haircut_price = 36
    total_price = (3 * women_haircut_price) + (2 * children_haircut_price)
    tip = 0.2 * total_price
    result = tip
    return result

print(solution())