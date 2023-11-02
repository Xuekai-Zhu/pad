def solution():
    """Johannes owns a vegetable shop, he sells cabbage for $2 per kilogram. If Johannes was able to earn $30 last Wednesday, $24 last Friday, and $42 today, how many kilograms of cabbage was he able to sell?"""
    wednesday_sales = 30
    friday_sales = 24
    today_sales = 42
    total_sales = wednesday_sales + friday_sales + today_sales
    cabbage_sales = total_sales / 2
    result = cabbage_sales
    return result

print(solution())