def solution():
    
    remy_sales = 55
    nick_sales = remy_sales - 6
    price_per_bottle = 0.5
    evening_sales = 55
    morning_sales = (remy_sales + nick_sales) * price_per_bottle
    difference = evening_sales - morning_sales
    result = difference
    return result

print(solution())