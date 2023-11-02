def solution():
    """Brandon sold 86 geckos last year. He sold twice that many the year before. How many geckos has Brandon sold in the last two years?"""
    # Calculate the number of geckos sold the year before last year
    geckos_before_last_year = 86 * 2

    # Calculate the total number of geckos sold in the last two years
    total_geckos_sold = geckos_before_last_year + 86

    # return the result
    result = total_geckos_sold
    return result

print(solution())