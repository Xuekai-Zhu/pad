def solution():
    num_geckos_last_year = 86
    num_geckos_year_before = num_geckos_last_year * 2

    # Calculate the total number of geckos sold in the last two years
    total_geckos_sold = num_geckos_last_year + num_geckos_year_before
    result = total_geckos_sold
    return result

print(solution())