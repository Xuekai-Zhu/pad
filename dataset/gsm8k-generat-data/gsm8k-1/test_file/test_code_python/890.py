def solution():
    """Last month, Tasha made $80 from selling lemonade and mowing lawns. The first week, she mowed Kamala's lawn thrice as many times as she did Joe's. The following week, she mowed Alba's lawn five times as she did Joe's. If Joe paid Tasha $6 for her work, how much did she make from lemonade sales?"""
    lawn_income = 6 * ((3 * 1) + (5 * 1))  # Joe paid Tasha $6 for her work on his lawn
    total_income = 80
    lemonade_income = total_income - lawn_income
    result = lemonade_income
    return result

print(solution())