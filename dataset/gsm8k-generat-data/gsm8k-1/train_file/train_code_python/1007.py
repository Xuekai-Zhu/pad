def solution():
    """Lana aims to sell 20 muffins at the bake sale. She sells 12 muffins in the morning. She sells another 4 in the afternoon. How many more muffins does Lana need to sell to hit her goal?"""
    total_goal = 20
    morning_sales = 12
    afternoon_sales = 4
    remaining_sales = total_goal - morning_sales - afternoon_sales
    result = remaining_sales
    return result

print(solution())