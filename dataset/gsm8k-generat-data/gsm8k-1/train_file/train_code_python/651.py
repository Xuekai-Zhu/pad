def solution():
    """Tanika is selling boxes of crackers for her scout troop's fund-raiser. On Saturday, she sold 60 boxes. On Sunday, she sold 50% more than on Saturday. How many boxes did she sell, in total, over the two days?"""
    saturday_sales = 60
    sunday_sales = saturday_sales * 1.5
    total_sales = saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())