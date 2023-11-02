def solution():
    current_sales = 327  # The store sold 327 televisions this Black Friday
    increase_per_year = 50  # The store sells 50 more televisions each year
    total_sales = current_sales + (increase_per_year * 3)  # Calculate total sales in three years
    result = total_sales
    return result

print(solution())