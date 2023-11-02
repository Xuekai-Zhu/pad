def solution():
    day1_sales = 45
    day2_sales = day1_sales + 20
    day3_sales = 2 * day2_sales - 10
    total_sales = day1_sales + day2_sales + day3_sales + x  # let x be the sales on the fourth day
    x = 350 - total_sales  # solve for x
    result = x
    return result

print(solution())