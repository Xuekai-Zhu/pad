def solution():
    """Remy sold 55 bottles of soda in the morning. Nick sold six fewer bottles of soda than Remy. The price per bottle is $.50. If their total evening sales are $55, how much more did they earn in the evening than in the morning?"""
    remy_sales = 55
    nick_sales = remy_sales - 6
    price_per_bottle = 0.5
    evening_sales = 55
    morning_sales = (remy_sales + nick_sales) * price_per_bottle
    difference = evening_sales - morning_sales
    result = difference
    return result

print(solution())