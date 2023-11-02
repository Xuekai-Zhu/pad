def solution():
    # Calculate morning sales
    morning_apple_sales = 40 * 1.5
    morning_orange_sales = 30 * 1
    morning_total_sales = morning_apple_sales + morning_orange_sales

    # Calculate afternoon sales
    afternoon_apple_sales = 50 * 1.5
    afternoon_orange_sales = 40 * 1
    afternoon_total_sales = afternoon_apple_sales + afternoon_orange_sales

    # Calculate total sales for the day
    total_sales = morning_total_sales + afternoon_total_sales
    result = total_sales
    return result

print(solution())