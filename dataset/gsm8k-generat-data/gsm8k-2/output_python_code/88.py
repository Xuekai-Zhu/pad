def solution():
    """Brandon sold 86 geckos last year. He sold twice that many the year before. How many geckos has Brandon sold in the last two years?"""
    last_year_sales = 86
    previous_year_sales = last_year_sales * 2
    total_sales = last_year_sales + previous_year_sales
    result = total_sales
    return result

print(solution())