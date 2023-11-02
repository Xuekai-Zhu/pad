def solution():
    """Lana aims to sell 20 muffins at the bake sale. She sells 12 muffins in the morning. She sells another 4 in the afternoon. How many more muffins does Lana need to sell to hit her goal?"""
    morning_sales = 12
    afternoon_sales = 4
    total_sales = morning_sales + afternoon_sales
    goal = 20
    remaining_sales = goal - total_sales
    result = remaining_sales
    return result

print(solution())