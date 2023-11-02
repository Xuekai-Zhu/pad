def solution():
    # Sales on the first day
    sales_first_day = 20 * 2  # James visits 20 houses and sells 2 items at each house

    # Sales on the second day
    sales_second_day = 40 * 2 * 0.8  # James visits 40 houses, sells to 80% of them, and sells 2 items at each house

    # Total sales
    total_sales = sales_first_day + sales_second_day
    result = total_sales
    return result

print(solution())