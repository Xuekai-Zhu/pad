def solution():
    """Shaniqua styles hair. For every haircut she makes $12 and for every style she makes $25. How many dollars would Shaniqua make if she gave 8 haircuts and 5 styles?"""
    haircut_price = 12
    style_price = 25
    num_haircuts = 8
    num_styles = 5
    total_income = (num_haircuts * haircut_price) + (num_styles * style_price)
    result = total_income
    return result

print(solution())