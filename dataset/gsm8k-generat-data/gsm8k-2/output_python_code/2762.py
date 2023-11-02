def solution():
    """On Friday, Markeesha sold 30 boxes of crackers for her scout troop's fundraiser. On Saturday, she sold twice as many as on Friday. On Sunday, she sold 15 fewer than Saturday. How many boxes did she sell over the three days?"""
    friday_sales = 30
    saturday_sales = 2 * friday_sales
    sunday_sales = saturday_sales - 15
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())