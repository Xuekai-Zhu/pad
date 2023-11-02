def solution():
    last_year_sales = 86  # Brandon sold 86 geckos last year
    sales_two_years_ago = last_year_sales * 2  # He sold twice that many the year before

    # Total geckos sold in the last two years
    total_sales = last_year_sales + sales_two_years_ago
    result = total_sales
    return result

print(solution())