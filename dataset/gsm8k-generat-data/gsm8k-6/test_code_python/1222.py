def solution():
    # Calculate the total sales for the morning
    morning_sales = 40 * 1.5 + 30 * 1  # 40 apples at $1.50 each and 30 oranges at $1 each

    # Calculate the total sales for the afternoon
    afternoon_sales = 50 * 1.5 + 40 * 1  # 50 apples at $1.50 each and 40 oranges at $1 each

    # Calculate the total sales for the day
    total_sales = morning_sales + afternoon_sales

    result = total_sales
    return result

print(solution())