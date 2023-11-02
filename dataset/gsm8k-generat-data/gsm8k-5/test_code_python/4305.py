def solution():
    monday_sales = 5  # Gabrielle sells 5 crates on Monday
    tuesday_sales = 2 * monday_sales  # Gabrielle sells 2 times as many as Monday on Tuesday
    wednesday_sales = tuesday_sales - 2  # Gabrielle sells 2 fewer than Tuesday on Wednesday
    thursday_sales = tuesday_sales / 2  # Gabrielle sells half as many as Tuesday on Thursday
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales  # Calculate total sales for four days
    result = total_sales
    return result

print(solution())