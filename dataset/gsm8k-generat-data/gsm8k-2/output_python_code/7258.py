def solution():
    """Sally sold 20 cups of lemonade last week. She sold 30% more lemonade this week. How many cups of lemonade did she sell in total for both weeks?"""
    last_week_sales = 20
    this_week_sales = last_week_sales * 1.3
    total_sales = last_week_sales + this_week_sales
    result = total_sales
    return result

print(solution())