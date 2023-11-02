def solution():
    sasha_muffins = 30
    melissa_muffins = 4 * sasha_muffins
    total_muffins = sasha_muffins + melissa_muffins
    tiffany_muffins = total_muffins / 2

    # Calculate total sales from muffins
    total_sales = (sasha_muffins + melissa_muffins + tiffany_muffins) * 4
    sasha_sales = sasha_muffins * 4
    melissa_sales = melissa_muffins * 4
    tiffany_sales = tiffany_muffins * 4

    result = (sasha_sales, melissa_sales, tiffany_sales)
    return result

print(solution())