def solution():
    """Tameka is selling boxes of crackers for her scout troop. On Friday, she sold 40 boxes. On Saturday, she sold 10 fewer than twice that number. And on Sunday, she sold half as many as Sunday. How many boxes did she sell over the three days?"""
    friday_sales = 40
    saturday_sales = (2 * friday_sales) - 10
    sunday_sales = sunday_sales // 2
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())